const Wemo = require('wemo-client');
const samplingPeriod = 500;

function search() {
  let wemo = new Wemo();
  wemo.discover((deviceInfo) => {
    let client = wemo.client(deviceInfo);
    let reader = new Reader(client);
    reader.start();
  });
}

function getTime() {
  return new Date().getTime() / 1000;
}

class Reader {
  constructor(client) {
    this.client = client;
  }

  start() {
    setInterval(() => {
      this.read((err, values) => {
        let time = getTime();

        if (err) { console.log(err); return; }
        console.log(this.client.device.serialNumber,
            time,
            'power',
            parseFloat(values.instantPower));
      });
    }, samplingPeriod);
  }

  read(callback) {
    this.client.getInsightParams((err, binaryState, instantPower, insightParams) => {
      callback(err, {
        binaryState: binaryState,
        instantPower: instantPower,
        insightParams: insightParams
      });
    });
  }
}

search();
