var logging = {};

function getTime() {
  return new Date().getTime();
}

function logData(sensor, data) {
  var message = {
    'time': getTime()
  };
  for (var key in data) {
    message[sensor + '_' + key] = data[key];
  }
  app.publish(message);
}

function logValue(sensor, data) {
  var message = {
    'time': getTime()
  };
  message[sensor] = data;
  app.publish(message);
}

(function(){

  logging.logAccelerometerData = function(data) {
    logData('accel', data);
  };

  logging.logGyroscopeData = function(data) {
    logData('gyroscope', data);
  };

  logging.logMagnetometerData = function(data) {
    logData('magnetometer', data);
  };

  logging.logBarometerData = function(data) {
    logValue('pressure', data);
  };

  logging.logTemperatureData = function(data) {
    logValue('temperature', data);
  };

  logging.logHumidityData = function (data) {
    logValue('humidity', data);
  };

  logging.logSensorFusionData = function (data) {
    logData('sensor_fusion', data);
  };

})();
