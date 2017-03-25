function padToTwo(number) {
  if (number<=99) { number = ('00'+number).slice(-2); }
  return number;
}

function getDateString(time) {
  let date = new Date();
  if (time) {
    date = new Date(time);
  }
  let dateStr = [
    [date.getUTCFullYear(), padToTwo(date.getUTCMonth() + 1), padToTwo(date.getUTCDate())].join('-'),
    [
      [padToTwo(date.getUTCHours()), padToTwo(date.getUTCMinutes()), padToTwo(date.getUTCSeconds())].join(':'),
      date.getUTCMilliseconds()
    ].join('.')
  ].join(' ');

  return dateStr;
}

module.exports = getDateString;
