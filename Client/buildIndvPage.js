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
      document.getElementById('race1').innerHTML = "Race1: "+runnerData[loopNum].getAttribute('race1') //We need todo a loop here to check if != null
      document.getElementById('race2').innerHTML = "Race2: "+runnerData[loopNum].getAttribute('race2')
      document.getElementById('race3').innerHTML = "Race3: "+runnerData[loopNum].getAttribute('race3')
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
  document.body.appendChild(backButton);
  //Bind the back button

  backButton.addEventListener("click", function(s, xml = xmlSheet) {
    //console.log('Bounded');// -- making sure this function is running.
    ipcRenderer.send('buildRunnerPage', xml);
  });



})
//Start
ipcRenderer.send('buildIndvPage-Ready')
