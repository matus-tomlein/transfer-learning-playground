import paho.mqtt.client as mqtt
from bluepy.btle import *
import struct
from time import sleep, time
from tbsense import Thunderboard
import threading
import json


class Reporter:
    def __init__(self, client):
        self.client = client


    def report(self, device, values):
        t = int(time() * 1000)
        values['device'] = device
        values['time'] = t

        content = json.dumps(values)
        #print(content)
        self.client.publish('sensors', content)


def getThunderboards(reporter):
    scanner = Scanner(0)
    devices = scanner.scan(3)
    tbsense = dict()
    for dev in devices:
        scanData = dev.getScanData()
        for (adtype, desc, value) in scanData:
            if desc == 'Complete Local Name':
                if 'Thunder Sense #' in value:
                    deviceId = int(value.split('#')[-1])
                    tbsense[deviceId] = Thunderboard(dev, reporter)

    return tbsense

def sensorLoop(tb, devId):
    
    value = tb.char['power_source_type'].read()
    if ord(value) == 0x04:
        tb.coinCell = True

    while True:

        try:
            tb.readAndSendAll()
            tb.waitForNotifications()

        except Exception as err:
            print(err)
            return

        #sleep(0.1)


def dataLoop(thunderboards):
    threads = []
    for devId, tb in thunderboards.items():
        t = threading.Thread(target=sensorLoop, args=(tb, devId))
        threads.append(t)
        print('Starting thread {} for {}'.format(t, devId))
        t.start()

def search(reporter):
    while True:
        thunderboards = getThunderboards(reporter)
        if len(thunderboards) == 0:
            print("No Thunderboard Sense devices found!")
        else:
            dataLoop(thunderboards)

def on_connect(client, userdata, flags, rc):
    print('Connected to MQTT')

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

if __name__ == '__main__':
    client = mqtt.Client('thunderboard')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('matus.wv.cc.cmu.edu', 1883)
    reporter = Reporter(client)
    search(reporter)
    client.loop_forever()
