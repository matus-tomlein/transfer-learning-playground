var humidity = require('./humidity'),
    imu = require('./imu'),
    pressure = require('./pressure'),
    microphone = require('./microphone'),
    // uv = require('./uv'),

    mqtt = require('mqtt');

function start(deviceId) {
  
  client = mqtt.connect('mqtt://matus.wv.cc.cmu.edu');
  client.on('connect', function () {
  
    var sendData = function (data) {
      var time = new Date().getTime();
      data.device = deviceId;
      data.time = time;
      client.publish('sensors', JSON.stringify(data));
    };
  
    //humidity(sendData);
    imu(sendData);
    pressure(sendData);
    microphone(sendData);
    // uv(sendData);
  });

}

require('getmac').getMac(function (err, macAddress) {
  if (err) { console.log(err); return; }

  var deviceId = 'Matrix ' + macAddress.split(':').join('');
  console.log('Device ID:', deviceId);

  start(deviceId);
});
