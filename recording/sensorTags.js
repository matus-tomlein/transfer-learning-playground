const SensorTag = require('sensortag'),
      mqtt = require('mqtt');


function getTime() { return new Date().getTime(); }

function hashCode(str) {
  var hash = 0, i, chr, len;
  if (str.length === 0) return hash;
  for (i = 0, len = str.length; i < len; i++) {
    chr   = str.charCodeAt(i);
    hash  = ((hash << 5) - hash) + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
}


class SensorTagReader {
  constructor(client) {
    this.client = client;
    this.samplingPeriod = 100;
    this.slowSamplingPeriod = 1000;
  }

  addReading(time, tag, sensor, value) {
    let id = Math.abs(hashCode(tag.id) % 1000);
    let data = { time: time, device: 'TI SensorTag ' + id };
    if (value.x) {
      for (let key in value) {
        data[sensor + '_' + key] = value[key];
      }
    } else {
      data[sensor] = value;
    }
    client.publish('sensors', JSON.stringify(data));
  }

  setUpHumidityListeners(tag) {
    tag.enableHumidity((err) => {
      if (err) { console.error(err); return; }

      tag.notifyHumidity((err) => {
        if (err) { console.error(err); return; }

        tag.setHumidityPeriod(this.slowSamplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('humidityChange', (temperature, humidity) => {
            let time = getTime();
            this.addReading(time, tag, 'temperature', temperature);
            this.addReading(time, tag, 'humidity', humidity);
          });
        });
      });
    });
  }

  setUpPressureListeners(tag) {
    tag.enableBarometricPressure((err) => {
      if (err) { console.error(err); return; }

      tag.notifyBarometricPressure((err) => {
        if (err) { console.error(err); return; }

        tag.setBarometricPressurePeriod(this.samplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('barometricPressureChange', (pressure) => {
            let time = getTime();
            this.addReading(time, tag, 'pressure', pressure);
          });
        });
      });
    });
  }

  setUpLuxometerListeners(tag) {
    tag.enableLuxometer((err) => {
      if (err) { console.error(err); return; }

      tag.notifyLuxometer((err) => {
        if (err) { console.error(err); return; }

        tag.setLuxometerPeriod(this.slowSamplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('luxometerChange', (lux) => {
            let time = getTime();
            this.addReading(time, tag, 'light', lux);
          });
        });
      });
    });
  }

  setUpGyroListeners(tag) {
    tag.enableGyroscope((err) => {
      if (err) { console.error(err); return; }

      tag.notifyGyroscope((err) => {
        if (err) { console.error(err); return; }

        tag.setGyroscopePeriod(this.samplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('gyroscopeChange', (x, y, z) => {
            let time = getTime();
            this.addReading(time, tag, 'gyro', { x: x, y: y, z: z });
          });
        });
      });
    });
  }

  setUpAccelerometerListeners(tag) {
    tag.enableAccelerometer((err) => {
      if (err) { console.error(err); return; }

      tag.notifyAccelerometer((err) => {
        if (err) { console.error(err); return; }

        tag.setAccelerometerPeriod(this.samplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('accelerometerChange', (x, y, z) => {
            let time = getTime();
            this.addReading(time, tag, 'accel', { x: x, y: y, z: z });
          });
        });
      });
    });
  }

  setUpMagnetomerListeners(tag) {
    tag.enableMagnetometer((err) => {
      if (err) { console.error(err); return; }

      tag.notifyMagnetometer((err) => {
        if (err) { console.error(err); return; }

        tag.setMagnetometerPeriod(this.samplingPeriod, (err) => {
          if (err) { console.error(err); return; }

          tag.on('magnetometerChange', (x, y, z) => {
            let time = getTime();
            this.addReading(time, tag, 'mag', { x: x, y: y, z: z });
          });
        });
      });
    });
  }

  start() {
    SensorTag.discoverAll((tag) => {
      tag.connectAndSetUp((err) => {
        if (err) { console.error(err); return; }
        console.log('Found tag with id', tag.id);

        // this.setUpHumidityListeners(tag);
        // this.setUpPressureListeners(tag);
        this.setUpLuxometerListeners(tag);
        this.setUpGyroListeners(tag);
        this.setUpAccelerometerListeners(tag);
        this.setUpMagnetomerListeners(tag);
      });
    });
  }
}


let client = mqtt.connect('mqtt://transferlearning.andrew.cmu.edu');
client.on('connect', () => {
  let reader = new SensorTagReader(client);
  reader.start();
});
