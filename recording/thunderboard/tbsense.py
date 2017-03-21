from bluepy.btle import *
import struct
from time import sleep
import threading
import binascii


def accelerometerReadingThread(ble_service, tb):
      ble_service.setDelegate(BleDelegate(tb))

      return
      while True:
          if ble_service.waitForNotifications(1.0):
              continue


class BleDelegate(DefaultDelegate):
   def __init__(self, tb):
       DefaultDelegate.__init__(self)
       self.tb = tb

   def handleNotification(self, cHandle, data):
       values = struct.unpack('<hhh', data)
       x = values[0]
       y = values[1]
       z = values[2]
       self.tb.report({'accel_x': x, 'accel_y': y, 'accel_z': z})


class Thunderboard:

   def __init__(self, dev, reporter):
      self.dev  = dev
      self.reporter = reporter
      self.char = dict()
      self.name = ''
      self.session = ''
      self.coinCell = False

      # Get device name and characteristics

      scanData = dev.getScanData()

      for (adtype, desc, value) in scanData:
         if (desc == 'Complete Local Name'):
            self.name = value

      ble_service = Peripheral()
      ble_service.connect(dev.addr, dev.addrType)
      characteristics = ble_service.getCharacteristics()

      for k in characteristics:
         if k.uuid == '2a6e':
            self.char['temperature'] = k
            
         elif k.uuid == '2a6f':
            self.char['humidity'] = k
            
         elif k.uuid == '2a76':
            self.char['uvIndex'] = k
            
         elif k.uuid == '2a6d':
            self.char['pressure'] = k
            
         elif k.uuid == 'c8546913-bfd9-45eb-8dde-9f8754f4a32e':
            self.char['ambientLight'] = k

         elif k.uuid == 'c8546913-bf02-45eb-8dde-9f8754f4a32e':
            self.char['sound'] = k

         elif k.uuid == 'efd658ae-c401-ef33-76e7-91b00019103b':
            self.char['co2'] = k

         elif k.uuid == 'efd658ae-c402-ef33-76e7-91b00019103b':
            self.char['voc'] = k

         elif k.uuid == 'ec61a454-ed01-a5e8-b8f9-de9ec026ec51':
            self.char['power_source_type'] = k

         elif k.uuid == 'c4c1f6e2-4be5-11e5-885d-feff819cdc9f':
            self.char['accel'] = k

         # else:
            # print(k.uuid)


      notify = ble_service.getCharacteristics(uuid=self.char['accel'].uuid)[0]
      notify_handle = notify.getHandle() + 1

      setup_data = b"\x01\x00"
      ble_service.writeCharacteristic(notify_handle, setup_data, withResponse=True)
      ble_service.setDelegate(BleDelegate(self))
      self.ble_service = ble_service

      #accelerometerReadingThread(ble_service, self)
      #t = threading.Thread(target=accelerometerReadingThread, args=(ble_service,))
      #t.start()

   
   def readTemperature(self):
      value = self.char['temperature'].read()
      value = struct.unpack('<H', value)
      value = value[0] / 100
      return value

   def readHumidity(self):
      value = self.char['humidity'].read()
      value = struct.unpack('<H', value)
      value = value[0] / 100
      return value

   def readAmbientLight(self):
      value = self.char['ambientLight'].read()
      value = struct.unpack('<L', value)
      value = value[0] / 100
      return value

   def readUvIndex(self):
      value = self.char['uvIndex'].read()
      value = ord(value)
      return value

   def readCo2(self):
      value = self.char['co2'].read()
      value = struct.unpack('<h', value)
      value = value[0]
      return value

   def readVoc(self):
      value = self.char['voc'].read()
      value = struct.unpack('<h', value)
      value = value[0]
      return value

   def readSound(self):
      value = self.char['sound'].read()
      value = struct.unpack('<h', value)
      value = value[0] / 100
      return value

   def readPressure(self):
      value = self.char['pressure'].read()
      value = struct.unpack('<L', value)
      value = value[0] / 1000
      return value

   def waitForNotifications(self):
      self.ble_service.waitForNotifications(1.0)

   def readAndSendAll(self):
      temperature = self.readTemperature()
      humidity = self.readHumidity()
      light = self.readAmbientLight()
      sound = self.readSound()
      pressure = self.readPressure()

      self.report({
          'temperature': temperature,
          'pressure': pressure,
          'humidity': humidity,
          'light': light
      })

   def report(self, values):
      self.reporter.report(self.name, values)
