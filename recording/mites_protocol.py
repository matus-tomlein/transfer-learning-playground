from itertools import count
from enum import IntEnum
import struct
import json

# Keep updated with protocol.h

class SensorType(IntEnum):
    __n__ = count()
    ACCEL = next(__n__)
    MICROPHONE = next(__n__)
    EMI = next(__n__)
    TEMPERATURE = next(__n__)
    BAROMETER = next(__n__)
    HUMIDITY = next(__n__)
    ILLUMINATION = next(__n__)
    COLOR = next(__n__)
    MAGNETOMETER = next(__n__)
    WIFI_RSSI = next(__n__)
    IRMOTION = next(__n__)
    GEYE = next(__n__)
    MACADDR = next(__n__)
    NUM_SENSORS = next(__n__)
    RAW = 255
    
    def __str__(self):
        return str(self.name)

def sensortype_as_enum(s):
    return SensorType(int(s))

def SensorName(sensor_type):
    return str(SensorType(sensor_type))

class SensorDataType(IntEnum):
    __n__ = count()
    UINT8 = next(__n__)
    SINT8 = next(__n__)
    UINT16 = next(__n__)
    SINT16 = next(__n__)
    SINT32 = next(__n__)
    __n__ = count(8)
    FLOAT = next(__n__)

class SensorDataFormat(IntEnum):
    NO_ENDIAN = 0x00
    LITTLE_ENDIAN = 0x00
    BIG_ENDIAN = 0x80
    MASK = 0x80

header_fmt = '<BBBBI' # Need to update this format to match current protocol
header_size = struct.calcsize(header_fmt)
num_features = (3+1+1)*2 + (1+1+1+3+3+1+1+16)
fft_sensors = [
    SensorType.ACCEL,
    SensorType.MICROPHONE,
    SensorType.EMI,
]

stats_sensors = [
    SensorType.ACCEL,
    SensorType.MICROPHONE,
    SensorType.EMI,
    SensorType.TEMPERATURE,
    SensorType.BAROMETER,
    SensorType.HUMIDITY,
    SensorType.ILLUMINATION,
    SensorType.COLOR,
    SensorType.MAGNETOMETER,
    SensorType.WIFI_RSSI,
    SensorType.IRMOTION,
    SensorType.GEYE
]
target_feature_count = len(fft_sensors)+len(stats_sensors)

def decode_header(header):
    sensor_type, data_fmt, num_channels, feature_type, data_len = struct.unpack(header_fmt, header)

    format = SensorDataFormat.MASK & data_fmt
    datatype = (~SensorDataFormat.MASK) & data_fmt

    return SensorType(sensor_type), (datatype, format), num_channels, data_len, feature_type
