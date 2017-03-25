/**
 * This software is copyrighted by Bosch Connected Devices and Solutions GmbH, 2016.
 * The use of this software is subject to the XDK SDK EULA
 */
//lint -esym(956,*) /* Suppressing "Non const, non volatile static or external variable" lint warning*/

/* module includes ********************************************************** */

/* system header files */
#include <stdio.h>
#include <math.h>
/* additional interface header files */
#include "simplelink.h"
#include "BCDS_Basics.h"
#include "BCDS_Assert.h"
#include "FreeRTOS.h"
#include "timers.h"
#include "BLE_stateHandler_ih.h"
#include "BLE_serialDriver_ih.h"
#include "BCDS_WlanConnect.h"
#include "BCDS_NetworkConfig.h"
#include <Serval_Types.h>
#include <Serval_Basics.h>
#include <Serval_Ip.h>

/* interface header files */
#include "XdkSensorHandle.h"
#include "BCDS_PowerMgt.h"
#include "BCDS_Retcode.h"

#include "SendData.h"


/* own header files */
#include "MQTTClient.h"

/* constant definitions ***************************************************** */

#define BUFFER_SIZE        UINT8_C(60)
#define NOISE_PERIOD1      5
#define NOISE_PERIOD2      10

/* local variables ********************************************************** */


/* additional interface header files */
#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include "PTD_portDriver_ph.h"
#include "PTD_portDriver_ih.h"
#include "WDG_watchdog_ih.h"

/* paho header files */
#include "MQTTConnect.h"

/* constant definitions ***************************************************** */

/* local variables ********************************************************** */
// Buffers
static unsigned char buf[CLIENT_BUFF_SIZE];
static unsigned char readbuf[CLIENT_BUFF_SIZE];

static uint8_t clientDataGetFlag = NUMBER_UINT8_ZERO;
static uint32_t clientMessageId = 0;

// Subscribe topics variables
char clientTopicRed[CLIENT_BUFF_SIZE];
char clientTopicOrange[CLIENT_BUFF_SIZE];
char clientTopicYellow[CLIENT_BUFF_SIZE];
char clientTopicDataGet[CLIENT_BUFF_SIZE];
char clientTopicDataStream[CLIENT_BUFF_SIZE];
const char *clientTopicDataStream_ptr = TOPIC_DATA_STREAM;

Network n;
Client c;

DataBuffer sensorStreamBuffer;  // Data Stream Bufer

static Accelerometer_XyzData_T accelData;
static Gyroscope_XyzData_T gyroData;
static uint32_t milliLuxData;
static Magnetometer_XyzData_T magData;
static Environmental_Data_T environmentData;
//static uint32_t noiseRaw;

static uint32_t  noiseDbSpl;

static uint8_t  noisePeriod1Cnt;
static uint8_t  noisePeriod2Cnt;
static uint8_t  noisePeriodCnt;

static uint32_t noiseRawAvg1[NOISE_PERIOD1] = { 0 };
static uint32_t noiseRawAvg2[NOISE_PERIOD2] = { 0 };
static uint32_t noiseRawAveraged[PERIOD] = { 0 };

/**
 * This buffer holds the data to be sent to server via UDP
 * */
static uint8_t bsdBuffer_mau[BUFFER_SIZE] = { (uint8_t) ZERO };

/**
 * Timer handle for connecting to wifi and obtaining the IP address
 */
xTimerHandle wifiConnectTimerHandle_gdt = NULL;

/**
 * Timer handle for periodically sending data over wifi
 */
xTimerHandle wifiSendTimerHandle = NULL;

/**
 * Timer handle for noise sampling
 */
xTimerHandle noiseSampleTimerHandle = NULL;

/* global variables ********************************************************* */

/* inline functions ********************************************************* */



/* local functions ********************************************************** */

static void sampleNoiseSensor(xTimerHandle xTimer);

/**
 *  @brief
 *      Function to initialize the wifi network send application. Create timer task
 *      to start WiFi Connect and get IP function after one second. After that another timer
 *      to send data periodically.
 */
void init(void)
{
	printf("Init 0\r\n");
    uint32_t Ticks = PERIOD*10;

    if (Ticks != UINT32_MAX) /* Validated for portMAX_DELAY to assist the task to wait Infinitely (without timing out) */
    {
        Ticks /= portTICK_RATE_MS;
    }
    if (UINT32_C(0) == Ticks) /* ticks cannot be 0 in FreeRTOS timer. So ticks is assigned to 1 */
    {
        Ticks = UINT32_C(1);
    }

    printf("Init 1\r\n");

    /* Initialize sensors */

    accelerometerSensorInit();
    gyroSensorInit();
    lightsensorInit();
    noiseSensorInit();
    magnetometerSensorInit();
    environmentSensorInit();
    orientationSensorInit();


    /* create timer task*/
    wifiConnectTimerHandle_gdt = xTimerCreate((char * const ) "wifiConnect", Ticks, TIMER_AUTORELOAD_OFF, NULL, wifiConnectGetIP);
    wifiSendTimerHandle = xTimerCreate((char * const ) "wifiSend", Ticks, TIMER_AUTORELOAD_ON, NULL, wifiSend);
    noiseSampleTimerHandle = xTimerCreate((char * const ) "noiseSample", Ticks, TIMER_AUTORELOAD_ON, NULL, sampleNoiseSensor);

    if ((wifiConnectTimerHandle_gdt != NULL) && (wifiSendTimerHandle != NULL))
    {
        /*start the wifi connect timer*/
        if ( xTimerStart(wifiConnectTimerHandle_gdt, TIMERBLOCKTIME) != pdTRUE)
        {
            assert(false);
        }
    }
    else
    {
        /* Assertion Reason: "Failed to create timer task during initialization"   */
        assert(false);
    }
}

/**
 * @brief This is a template function where the user can write his custom application.
 *
 */
void appInitSystem(xTimerHandle xTimer)
{
    BCDS_UNUSED(xTimer);

    printf("Hello world\r\n");
    /*Call the WNS module init API */
    init();
}

static void sampleNoiseSensor(xTimerHandle xTimer) {
	BCDS_UNUSED(xTimer);

	readNoiseSensor(&noiseDbSpl);
}

static void sampleAndStoreSensorData(void) {

	readAccelerometerData(&accelData);
	readGyroData(&gyroData);
	readLightSensor(&milliLuxData);
	readMagnetometerSensor(&magData);
	readEnvironmentSensor(&environmentData);
}


/**
 * @brief Opening a UDP client side socket and sending data on a server port
 *
 * This function opens a UDP socket and tries to connect to a Server SERVER_IP
 * waiting on port SERVER_PORT.
 * Then the function will send periodic UDP packets to the server.
 * 
 * @param[in] port
 *					destination port number
 *
 * @return         returnTypes_t:
 *                                  SOCKET_ERROR: when socket has not opened properly
 *                                  SEND_ERROR: when 0 transmitted bytes or send error
 *                                  STATUS_OK: when UDP sending was successful
 */

void sendMqttData() {
	if(sensorStreamBuffer.length > NUMBER_UINT32_ZERO)
	{
		MQTTMessage msg;
		msg.id = clientMessageId++;
		msg.qos = 0;
		msg.payload = sensorStreamBuffer.data;
		msg.payloadlen = sensorStreamBuffer.length;
		MQTTPublish(&c, clientTopicDataStream_ptr, &msg);

		memset(sensorStreamBuffer.data, 0x00, SENSOR_DATA_BUF_SIZE);
		sensorStreamBuffer.length = NUMBER_UINT32_ZERO;
	}
	else if(clientDataGetFlag) {
		//sensorStreamData(pvParameters);
		//clientDataGetFlag = DISABLED;
	}
	else {
		MQTTYield(&c, CLIENT_YIELD_TIMEOUT);
	}
}

static returnTypes_t bsdUdpClient()
{
	sensorStreamBuffer.length += sprintf(
				sensorStreamBuffer.data + sensorStreamBuffer.length,
				"{\"device\":\"matrix_1\",\"accel_x\":%ld,\"accel_y\":%ld,\"accel_z\":%ld,\"gyro_x\":%ld,\"gyro_y\":%ld,\"gyro_z\":%ld,\"magnet_x\":%ld,\"magnet_y\":%ld,\"magnet_z\":%ld,\"light_lux\":%.3f,\"temp_c\":%.3f,\"press_p\":%ld,\"humidity\":%ld,\"noise\":%ld}",
				accelData.xAxisData,
				accelData.yAxisData,
				accelData.zAxisData,
				gyroData.xAxisData,
				gyroData.yAxisData,
				gyroData.zAxisData,
				magData.xAxisData,
				magData.yAxisData,
				magData.zAxisData,
				milliLuxData / 1000.0,
				environmentData.temperature / 1000.0,
				environmentData.pressure,
				environmentData.humidity,
				noiseDbSpl
			);

	sendMqttData();

	return (STATUS_OK);
}
/**
 *  @brief
 *      Function to periodically send data over WiFi as UDP packets. This is run as an Auto-reloading timer.
 *
 *  @param [in ] xTimer - necessary parameter for timer prototype
 */
static void wifiSend(xTimerHandle xTimer)
{
    BCDS_UNUSED(xTimer);

    sampleAndStoreSensorData();

    if (STATUS_OK != bsdUdpClient())
    {
        /* assertion Reason:  "Failed to  send udp packet" */
        assert(false);
    }
}

/**
 *  @brief
 *      Function to connect to wifi network and obtain IP address
 *
 *  @param [in ] xTimer
 */
static void wifiConnectGetIP(xTimerHandle xTimer)
{
    BCDS_UNUSED(xTimer);

    NetworkConfig_IpSettings_T myIpSettings;
    memset(&myIpSettings, (uint32_t) 0, sizeof(myIpSettings));
    char ipAddress[PAL_IP_ADDRESS_SIZE] = { 0 };
    Ip_Address_T* IpaddressHex = Ip_getMyIpAddr();
    WlanConnect_SSID_T connectSSID;
    WlanConnect_PassPhrase_T connectPassPhrase;
    Retcode_T ReturnValue = (Retcode_T)RETCODE_FAILURE;
    int32_t Result = INT32_C(-1);

    if (RETCODE_OK != WlanConnect_Init())
    {
        printf("Error occurred initializing WLAN \r\n ");
        return;
    }

    printf("Connecting to %s \r\n ", WLAN_CONNECT_WPA_SSID);

    connectSSID = (WlanConnect_SSID_T) WLAN_CONNECT_WPA_SSID;
    connectPassPhrase = (WlanConnect_PassPhrase_T) WLAN_CONNECT_WPA_PASS;
    ReturnValue = NetworkConfig_SetIpDhcp(NULL);
    if (ReturnValue)
    {
        printf("Error in setting IP to DHCP\n\r");
        return;
    }

    if (RETCODE_OK == WlanConnect_WPA(connectSSID, connectPassPhrase, NULL))
//    if (RETCODE_OK == WlanConnect_Open(connectSSID, NULL))
    {
        ReturnValue = NetworkConfig_GetIpSettings(&myIpSettings);
        if (RETCODE_OK == ReturnValue)
        {
            *IpaddressHex = Basics_htonl(myIpSettings.ipV4);
            Result = Ip_convertAddrToString(IpaddressHex, ipAddress);
            if (Result < 0)
            {
                printf("Couldn't convert the IP address to string format \r\n ");
                return;
            }
            printf("Connected to WPA network successfully. \r\n ");
            printf(" Ip address of the device: %s \r\n ", ipAddress);
        }
        else
        {
            printf("Error in getting IP settings\n\r");
            return;
        }

    }
    else
    {
        printf("Error occurred connecting %s \r\n ", WLAN_CONNECT_WPA_SSID);
        return;
    }


    clientInit();


    /* After connection start the wifi sending timer*/
    if (xTimerStart(wifiSendTimerHandle, TIMERBLOCKTIME) != pdTRUE)
    {
        assert(false);
    }

    /* Initialize the counters for the noise sampling */
	noisePeriod1Cnt = NOISE_PERIOD1-1;
	noisePeriod2Cnt = NOISE_PERIOD2-1;
	noisePeriodCnt = PERIOD-1;

    /* Start sampling the noise sensor */
    if (xTimerStart(noiseSampleTimerHandle, TIMERBLOCKTIME) != pdTRUE)
    {
        assert(false);
    }

}


/**
 * @brief Initializes the MQTT Paho Client, set up subscriptions and initializes the timers and tasks
 *
 * @return NONE
 */
void clientInit(void)
{
	/* Initialize Variables */
    int rc = 0;
    NewNetwork(&n);
    ConnectNetwork(&n, MQTT_BROKER_NAME, MQTT_PORT);
    MQTTClient(&c, &n, 1000, buf, CLIENT_BUFF_SIZE, readbuf, CLIENT_BUFF_SIZE);

    /* Configure the MQTT Connection Data */
    MQTTPacket_connectData data = MQTTPacket_connectData_initializer;
    data.willFlag = 0;
    data.MQTTVersion = 3;
    data.clientID.cstring = MQTT_CLIENT_ID;
    data.keepAliveInterval = 100;
    data.cleansession = 1;

    printf("Connecting to %s %d\r\n", MQTT_BROKER_NAME, MQTT_PORT);

    /* Connect to the MQTT Broker */
    rc = MQTTConnect(&c, &data);

    return;
}

/**
 * @brief Disconnect from the MQTT Client
 *
 * @return NONE
 */
void clientDeinit(void)
{
    MQTTDisconnect(&c);
    n.disconnect(&n);
}

/* global functions ********************************************************* */

/** ************************************************************************* */