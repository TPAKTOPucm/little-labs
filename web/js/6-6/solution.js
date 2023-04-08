function setTime(totalSeconds) {
  document.getElementById('seconds').setAttribute('value', totalSeconds)
  document.getElementById('minutes').setAttribute('value', Math.floor(totalSeconds / 60))
  document.getElementById('hours').setAttribute('value', Math.floor(totalSeconds / 3600))
  document.getElementById('days').setAttribute('value', Math.floor(totalSeconds / 86400))
}

function fromSeconds() {
  setTime(parseInt(document.getElementById('seconds').value))
}

function fromMinutes() {
  setTime(parseInt(document.getElementById('minutes').value)*60)
}

function fromHours() {
  setTime(parseInt(document.getElementById('hours').value)*3600)
}

function fromDays() {
  setTime(parseInt(document.getElementById('days').value)*86400)
}