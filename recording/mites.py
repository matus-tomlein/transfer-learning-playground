#!/usr/bin/env python3
# -*- coding: utf8 -*-

''' Python server to receive data from one or more Supersensor units. '''
from time import time
import numpy as np
import pandas as pd
import json
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
import mites_protocol as protocol

to_numpy_dtype = {
    protocol.SensorDataType.UINT8: 'u1',
    protocol.SensorDataType.SINT8: 'i1',
    protocol.SensorDataType.UINT16: 'u2',
    protocol.SensorDataType.SINT16: 'i2',
    protocol.SensorDataType.SINT32: 'i4',
    protocol.SensorDataType.FLOAT: 'f4',
}

with open('settings.json') as data_file:    
    settings = json.load(data_file)


class RawDataStream():

    def __init__(self, header, data):
        self.header = header
        self.data = data


class CsvWriter:

    def __init__(self, device_id, sensor_name, feature_type):
        self.device_id = device_id
        self.sensor_name = str(sensor_name)
        self.feature_type = feature_type
        if self.feature_type == 0:
            self.feature_name = '_fft'
        else:
            self.feature_name = '_sst'
        self.written_header = False

    def write_values(self, values):
        if not self.written_header:
            self.written_header = True
            headers = ['']
            for i in range(len(values)):
                for n in range(len(values[i])):
                    headers.append(self.sensor_name + self.feature_name + '_' + str(i) + '_' + str(n))
            self.write(','.join(headers))

        items = [str(item) for sublist in values for item in sublist]
        t = str(pd.to_datetime(time(), unit='s'))
        items = [t] + items
        self.write(','.join(items))

    def file_name(self):
        path = settings['save_to_folder']
        path += '/' + self.device_id + '_'
        path += self.sensor_name + self.feature_name + '.csv'
        return path

    def write(self, text):
        with open(self.file_name(), 'a+') as file:
            file.write(text + "\n")


csv_writers = {}


class DataHandler(StreamRequestHandler):

    def __init__(self, *kargs):
        StreamRequestHandler.__init__(self, *kargs)

    def readall(self, sz):
        res = bytearray(sz)
        view = memoryview(res)
        pos = 0
        while pos < sz:
            pos += self.rfile.readinto(view[pos:])

        return res

    def report_sensor_values(self, sensor_type, feature_type, data):
        device_id = self.client_address[0]
        key = device_id + str(sensor_type) + str(feature_type)

        if key in csv_writers:
            csv_writers[key].write_values(data.T)
        else:
            writer = CsvWriter(device_id, sensor_type, feature_type)
            csv_writers[key] = writer
            writer.write_values(data.T)

        return

    def handle_one(self):
        header = self.readall(protocol.header_size)
        sensor_type, (data_type, data_fmt), num_channels, data_len, feature_type = protocol.decode_header(header)
        data = self.readall(data_len)
        big_endian = (data_fmt == protocol.SensorDataFormat.BIG_ENDIAN)
        dtype = ('>' if big_endian else '<') + to_numpy_dtype[data_type]
        arr = np.frombuffer(data, dtype=dtype).reshape((-1, num_channels))
        self.raw = RawDataStream(header, data)
        self.report_sensor_values(sensor_type, feature_type, arr)

    def handle(self):
        print("Got client: {0}".format(self.client_address))
        while 1:
            try:
                self.handle_one()
            except Exception:
                import traceback
                traceback.print_exc()
                break


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True
    daemon_threads = True
    pass


if __name__ == '__main__':
    HOST, PORT = '', 6204
    server = ThreadedTCPServer((HOST, PORT), DataHandler)
    server.serve_forever()
