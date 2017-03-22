const mqtt = require('mqtt'),
      _ = require('underscore');

const fs = require('fs');
const getDateString = require('./helpers/getDateString');
const settings = JSON.parse(fs.readFileSync('settings.json', 'utf8'));
const folderPath = settings.save_to_folder;

let client = mqtt.connect('mqtt://matus.wv.cc.cmu.edu');
client.on('connect', () => {
  client.subscribe('sensors');
});

let writtenToFiles = {};
let devicesOnline = {};

client.on('message', (topic, message) => {
  let receivedAt = getDateString();

  let data = JSON.parse(message.toString());
  devicesOnline[data.device] = true;

  let keys = Object.keys(data);
  keys = _.without(keys, 'device');
  keys = _.sortBy(keys);

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
});

setInterval(() => {
  console.log('Online:', Object.keys(devicesOnline).join(', '));
  devicesOnline = {};
}, 2000);