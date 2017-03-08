const SensorTag = require('sensortag');

let samplingPeriod = 100;
let numberOfExpectedTags = 4; // won't start writing data until all are connected
let tags = 0;

let data = {
  tags: [],
  readings: [],
  activities: []
};

function getTime() {
  return new Date().getTime() / 1000;
}

function addReading(time, tag, sensor, value) {
  if (tags == numberOfExpectedTags) {
    if (value.x) {
      console.log(tag.id, time, sensor + '_x', value.x);
      console.log(tag.id, time, sensor + '_y', value.y);
      console.log(tag.id, time, sensor + '_z', value.z);
    } else {
      console.log(tag.id, time, sensor, value);
    }
  }
}

function setUpHumidityListeners(tag) {
  tag.enableHumidity(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyHumidity(function (err) {
      if (err) { console.error(err); return; }

      tag.setHumidityPeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('humidityChange', function (temperature, humidity) {
          let time = getTime();
          addReading(time, tag, 'temperature', temperature);
          addReading(time, tag, 'humidity', humidity);
        });
      });
    });
  });
}

function setUpPressureListeners(tag) {
  tag.enableBarometricPressure(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyBarometricPressure(function (err) {
      if (err) { console.error(err); return; }

      tag.setBarometricPressurePeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('barometricPressureChange', function (pressure) {
          let time = getTime();
          addReading(time, tag, 'pressure', pressure);
        });
      });
    });
  });
}

function setUpLuxometerListeners(tag) {
  tag.enableLuxometer(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyLuxometer(function (err) {
      if (err) { console.error(err); return; }

      tag.setLuxometerPeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('luxometerChange', function (lux) {
          let time = getTime();
          addReading(time, tag, 'luxometer', lux);
        });
      });
    });
  });
}

function setUpGyroListeners(tag) {
  tag.enableGyroscope(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyGyroscope(function (err) {
      if (err) { console.error(err); return; }

      tag.setGyroscopePeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('gyroscopeChange', function (x, y, z) {
          let time = getTime();
          addReading(time, tag, 'gyroscope', { x: x, y: y, z: z });
        });
      });
    });
  });
}

function setUpAccelerometerListeners(tag) {
  tag.enableAccelerometer(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyAccelerometer(function (err) {
      if (err) { console.error(err); return; }

      tag.setAccelerometerPeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('accelerometerChange', function (x, y, z) {
          let time = getTime();
          addReading(time, tag, 'accelerometer', { x: x, y: y, z: z });
        });
      });
    });
  });
}

function setUpMagnetomerListeners(tag) {
  tag.enableMagnetometer(function (err) {
    if (err) { console.error(err); return; }

    tag.notifyMagnetometer(function (err) {
      if (err) { console.error(err); return; }

      tag.setMagnetometerPeriod(samplingPeriod, function (err) {
        if (err) { console.error(err); return; }

        tag.on('magnetometerChange', function (x, y, z) {
          let time = getTime();
          addReading(time, tag, 'magnetometer', { x: x, y: y, z: z });
        });
      });
    });
  });
}

SensorTag.discoverAll((tag) => {
  tag.connectAndSetUp((err) => {
    if (err) { console.error(err); return; }
    // console.log('Found tag with id', tag.id);

    data.tags.push({ id: tag.id });
    tags += 1;

    // setUpHumidityListeners(tag);
    // setUpPressureListeners(tag);
    // setUpLuxometerListeners(tag);
    setUpGyroListeners(tag);
    setUpAccelerometerListeners(tag);
    setUpMagnetomerListeners(tag);
  });
});
