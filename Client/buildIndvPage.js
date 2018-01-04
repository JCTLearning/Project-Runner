// buildIndvPage.js builds a runner page based on input
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;


ipcRenderer.on('continue', (event, runnerID, xmlSheet) => {
  console.log(xmlSheet)
  console.log(runnerID)
  var xmldocString = "runnerData/" + xmlSheet;
  console.log(xmldocString);
  var request = new XMLHttpRequest();
  request.open("GET", xmldocString, false);
  request.send();
  var xmlDoc = request.responseXML;
  console.log(xmlDoc)
  var runners = xmlDoc.childNodes[0];
  var loopNum = 0
  var runnerData = runners.getElementsByTagName("Data")
  var totalRunners = runnerData.length;

  while (loopNum != totalRunners) {
    if (runnerData[loopNum].getAttribute('id') == runnerID) {
      //Display Stats
      document.getElementById('runnerName').innerHTML = runnerData[loopNum].getAttribute('name') // Add a way to get back home
      break // Break the loop
    }
    // Isn't the number we were looking for
    loopNum = loopNum + 1
  }
})
ipcRenderer.send('buildIndvPage-Ready')
