// buildIndvPage.js builds a runner page based on input
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;
//let xmlSheet = 'null'

ipcRenderer.on('continue', (event, runnerID, xmlSheet) => {

  //console.log(xmlSheet)
  //console.log(runnerID)
  var xmldocString = "runnerData/" + xmlSheet;
  //console.log(xmldocString);
  var request = new XMLHttpRequest();
  request.open("GET", xmldocString, false);
  request.send();
  var xmlDoc = request.responseXML;
  //console.log(xmlDoc)
  var runners = xmlDoc.childNodes[0];
  var loopNum = 0
  var runnerData = runners.getElementsByTagName("Data")
  var totalRunners = runnerData.length;

  while (loopNum != totalRunners) {
    if (runnerData[loopNum].getAttribute('id') == runnerID) {
      //Display Stats
      document.getElementById('runnerName').innerHTML = runnerData[loopNum].getAttribute('name') // Add a way to get back home
      document.getElementById('id').innerHTML = "ID: "+runnerData[loopNum].getAttribute('id')
      document.getElementById('mile').innerHTML = "Mile Time: "+runnerData[loopNum].getAttribute('mile') //We need todo a loop here to check if != null
      document.getElementById('mile2').innerHTML = "Two Mile Time: "+runnerData[loopNum].getAttribute('mile2')
      document.getElementById('meter500').innerHTML = "500 meters Time: "+runnerData[loopNum].getAttribute('meter500')
      document.getElementById('meter800').innerHTML = "800 meters Time: "+runnerData[loopNum].getAttribute('meter800')
      document.getElementById('meters1500').innerHTML = "1500 meters Time: "+runnerData[loopNum].getAttribute('meters1500')
      document.getElementById('meters1600').innerHTML = "1600 meters Time: "+runnerData[loopNum].getAttribute('meters1600')
      document.getElementById('meters3000').innerHTML = "3000 meters Time: "+runnerData[loopNum].getAttribute('meters3000')
      document.getElementById('vdotData').innerHTML = "Overall VDOT Based Upon These Times: "+runnerData[loopNum].getAttribute('vdotData')
      /**
      So what we can do here is start creating elements // divs to hold this information in, so we can make it "pretty" for the users.
      Each piece of data can go into a element and what data is in there should look like this --
      <Data name="John Rancer" id = "1" race1="10:42" race2="9:50" race3="10:30" />
      I wanna add a 4 data set, and set it to a string, for Coach notes... Maybe try this once we get things pretty y'know.
      **/
      break // Break the loop
    }
    // Isn't the number we were looking for
    loopNum = loopNum + 1
  }
  var backButton = document.createElement("button");
  backButton.innerHTML = 'Back'
  backButton.id = 'backButtonId'
  backButton.className = 'sysButton'
  document.getElementById('mainBody').appendChild(backButton);
  //Bind the back button

  backButton.addEventListener("click", function(s, xml = xmlSheet) {
    //console.log('Bounded');// -- making sure this function is running.
    ipcRenderer.send('buildRunnerPage', xml);
  });



})
//Start
ipcRenderer.send('buildIndvPage-Ready')
