const mqtt = require('mqtt'),
      _ = require('underscore'),
      ws = require("nodejs-websocket");

const fs = require('fs');
const getDateString = require('./helpers/getDateString');
const settings = JSON.parse(fs.readFileSync('settings.json', 'utf8'));
const folderPath = settings.save_to_folder;

let client = mqtt.connect('mqtt://transferlearning.andrew.cmu.edu');
client.on('connect', () => {
  client.subscribe('sensors');
});

let writtenToFiles = {};
let devicesOnline = {};

function processMessage(data) {
  let receivedAt = getDateString();
  if (data.time) {
    data.time = getDateString(data.time);
  }

  devicesOnline[data.device] = true;

  let keys = Object.keys(data);
  keys = _.without(keys, 'device');
  keys = _.sortBy(keys);

  let zeroValuesCount = 0;
  keys.forEach((key) => { if (data[key] == 0) { zeroValuesCount += 1; } });
  if (zeroValuesCount > 2) { console.log('Getting zero values from', data.device); }

  let fileName = _.uniq(keys.map((s) => { return s.substring(0, 3); })).join('_');
  fileName = data.device + '_' + fileName;
  let filePath = folderPath + '/' + fileName + '.csv';

  let appendToFile = () => {
    let values = keys.map((key) => { return data[key]; });
    values.unshift(receivedAt);
    let str = values.join(',') + '\n';

    fs.appendFile(filePath, str, (err) => {
      if (err) console.error(err);
    });
  };

  if (writtenToFiles[fileName]) {
    appendToFile();
  } else {
    writtenToFiles[fileName] = true;

    fs.stat(filePath, (err) => {
      if (err == null) { // file exists
        appendToFile();
      }

      else { // file doesn't exist yet
        let header = ',' + keys.join(',') + '\n';
        fs.writeFile(filePath, header, (err) => {
          if (err) { console.log(err); return; }
          appendToFile();
        });
      }
    });
  }
}

client.on('message', (topic, message) => {
  let data = JSON.parse(message.toString());
  processMessage(data);
});

ws.createServer(function (conn) {
  conn.on('text', function (str) {
    processMessage(JSON.parse(str));
  });
  conn.on('close', function (code, reason) {
    console.log('Connection closed');
  });
}).listen(8001);

console.log('Listening on MQTT and WS port 8001');

setInterval(() => {
  let keys = Object.keys(devicesOnline);
  console.log(keys.length, '-', _.sortBy(keys).join(', '));
  devicesOnline = {};
}, 2000);
