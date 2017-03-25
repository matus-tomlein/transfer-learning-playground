var humidity = require('./humidity'),
    imu = require('./imu'),
    pressure = require('./pressure'),
    // uv = require('./uv'),

    mqtt = require('mqtt');

var deviceId = 'matrix_1';

client = mqtt.connect('mqtt://matus.wv.cc.cmu.edu');
client.on('connect', function () {

  var sendData = function (data) {
    let time = new Date().getTime();
    data.device = deviceId;
    data.time = time;
    client.publish('sensors', JSON.stringify(data));
  };

  humidity(sendData);
  imu(sendData);
  pressure(sendData);
  // uv(sendData);
});
