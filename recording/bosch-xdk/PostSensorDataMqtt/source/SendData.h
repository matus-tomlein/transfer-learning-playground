/**
 * This software is copyrighted by Bosch Connected Devices and Solutions GmbH, 2016.
 * The use of this software is subject to the XDK SDK EULA
 */

/* header definition ******************************************************** */
#ifndef XDK110_SENDDATAOVERUDP_H_
#define XDK110_SENDDATAOVERUDP_H_

#include "Sensors.h"

#include "MQTTClient.h"

/* local interface declaration ********************************************** */

/* local type and macro definitions */
typedef enum returnTypes_e
{
    STATUS_NOT_OK,
    STATUS_OK,
    SOCKET_ERROR,
    SEND_ERROR
} returnTypes_t;

#define ONESECONDDELAY UINT32_C(1000) 	            /**< Macro to represent one second time unit*/
#define FIVESECONDDELAY UINT32_C(5000)              /**< Macro to represent five second time unit*/

#define TIMERBLOCKTIME UINT32_MAX             /**< Macro used to define block time of a timer*/
#define ZERO    UINT8_C(0)  			            /**< Macro to define value zero*/
#define TIMER_AUTORELOAD_ON             UINT32_C(1)             /**< Auto reload of timer is enabled*/
#define TIMER_AUTORELOAD_OFF            UINT32_C(0)             /**< Auto reload of timer is disabled*/

#warning Please provide WLAN related configurations, with valid SSID & WPA key and server ip address where packets are to be sent in the below macros.
/** Network configurations */
#define WLAN_CONNECT_WPA_SSID                "giotto"         /**< Macros to define WPA/WPA2 network settings */
#define WLAN_CONNECT_WPA_PASS                "connectedthingswean4120"      /**< Macros to define WPA/WPA2 network settings */

#define DEVICE_ID 1

/** IP addressed of server side socket.Should be in long format, E.g: 0xc0a80071 == 192.168.0.113 */
//#define SERVER_IP         UINT32_C(0xC0A80071)
//#define SERVER_IP         UINT32_C(0xAC140A02)
//#define SERVER_PORT        UINT16_C(6666)           /**< Port number on which server will listen */

#define PERIOD             10

#define	MQTT_CLIENT_ID	    "xdk1"            /**< MQTT Client ID */
#define MQTT_BROKER_NAME    "transferlearning.andrew.cmu.edu"  /**< MQTT Broker */
#define MQTT_PORT           1883                          /**< MQTT Port Number */

#define CLIENT_YIELD_TIMEOUT              10


#define XDK_PAHO_DEMO_REVISION       "0.2.0"

#define NUMBER_UINT8_ZERO		     UINT8_C(0)     /**< Zero value */
#define NUMBER_UINT32_ZERO 		     UINT32_C(0)    /**< Zero value */
#define NUMBER_UINT16_ZERO 		     UINT16_C(0)    /**< Zero value */
#define NUMBER_INT16_ZERO 		     INT16_C(0)     /**< Zero value */

#define POINTER_NULL 			     NULL          /**< ZERO value for pointers */

#define TIMER_AUTORELOAD_ON          1             /**< Auto reload timer */
#define TIMER_AUTORELOAD_OFF         0             /**< One Shot Timer */

#define ENABLED         1
#define DISABLED        0


/* Paho Client type and macro definitions */
#define CLIENT_TASK_STACK_SIZE            1024
#define CLIENT_TASK_PRIORITY              1

#define CLIENT_BUFF_SIZE                  1000
#define CLIENT_YIELD_TIMEOUT              10

#define TOPIC_DATA_STREAM        "sensors"

#define	MQTT_CLIENT_ID	    "xdk1"            /**< MQTT Client ID */
#define MQTT_BROKER_NAME    "transferlearning.andrew.cmu.edu"  /**< MQTT Broker */
#define MQTT_PORT           1883                          /**< MQTT Port Number */


// Default Data Configuration Settings
#define STREAM_RATE         100/portTICK_RATE_MS /**< Stream Data Rate in MS */
#define ACCEL_EN            ENABLED               /**< Accelerometer Data Enable */
#define GYRO_EN             ENABLED               /**< Gyroscope Data Enable */
#define MAG_EN              ENABLED               /**< Magnetometer Data Enable */
#define ENV_EN              ENABLED               /**< Environmental Data Enable */
#define LIGHT_EN            ENABLED               /**< Ambient Light Data Enable */

#define WDG_FREQ            1000
#define WDG_TIMEOUT         200

/* global function prototype declarations */
void clientInit(void);
void clientDeinit(void);
void clientStartTimer(void);
void clientStopTimer(void);

/* global variable declarations */
extern Network n;
extern Client c;


/* interface header files */
#include "FreeRTOS.h"
#include "timers.h"

/* Sensor type and macro definitions */
#define SENSOR_DATA_BUF_SIZE    1024

typedef struct {
	uint32_t length;
	char data[SENSOR_DATA_BUF_SIZE];
} DataBuffer;

/* public global variable declarations */

// Data Buffers
extern DataBuffer sensorStreamBuffer;



/* local function prototype declarations */
/**
 *  @brief
 *      Function to connect to wifi network and obtain IP address
 *
 *  @param [in ] xTimer
 */
static void wifiConnectGetIP(xTimerHandle xTimer);
/**
 *  @brief
 *      Function to periodically send data over WiFi as UDP packets. This is run by an Auto-reloading timer.
 *
 *  @param [in ] xTimer
 */
static void wifiSend(xTimerHandle xTimer);

/* local module global variable declarations */

/* local inline function definitions */

#endif /* XDK110_SENDDATAOVERUDP_H_ */

/** ************************************************************************* */
