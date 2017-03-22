const readline = require('readline');
const getDateString = require('./helpers/getDateString');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const fs = require('fs');
const settings = JSON.parse(fs.readFileSync('settings.json', 'utf8'));
const filePath = settings.save_to_folder;

let lastId = 0;
let currentActivity = '-1';

function start() {
  setInterval(() => {
    fs.appendFile(filePath + '/activities.csv', [
      getDateString(),
      currentActivity
    ].join(',') + '\n', function (err) {
      if (err) console.error(err);
    });
  }, 100);

  rl.on('line', (line) => {
    if (line == 'q') {
      currentActivity = -1;
    } else {
      lastId += 1;
      currentActivity = lastId;

      fs.appendFile(filePath + '/activity_labels.csv', [
        currentActivity,
        line
      ].join(',') + '\n', function (err) {
        if (err) console.error(err);
      });
    }
  });
}

fs.writeFile(filePath + '/activities.csv', [
  '', 'id'
].join(',') + '\n', function(err) {
  if (err) { return console.error(err); }

  fs.writeFile(filePath + '/activity_labels.csv', [
    'id', 'label'
  ].join(',') + '\n', function(err) {
    if (err) { return console.error(err); }

    start();
  });
});
