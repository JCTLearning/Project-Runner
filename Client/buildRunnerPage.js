//buildRunnerPage.js
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;

ipcRenderer.on('buildDb', (event, xmlSheet) => {
  console.log(xmlSheet)
  main(xmlSheet);
})
function main(xmlSheet){
  xmlName = xmlSheet.replace('.xml', '')
  document.getElementById('titlePage').innerHTML = 'Dispay DB -- ' + xmlName
  document.getElementById('headerTitle').innerHTML = xmlName
  //open xmlSheet
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
    console.log(runnerData[loopNum]);
    x = runnerData[loopNum];
    runnerName = x.getAttribute("name");
    runnerId = x.getAttribute("id")
    var button =  document.createElement("button");
    button.innerHTML =  runnerName + " Details" //I guess we can put the adv vdot here. Then design each button :P
    button.id = runnerId

    document.body.appendChild(button);
    button.addEventListener('click',  function(s, y = this.id) {
      // Take Y (which is the xml file) and build a new page using is
      ipcRenderer.send('buildIndvPage', y)
    });
    // End of loop
    loopNum = loopNum +  1

  }


  }
ipcRenderer.send('buildRunnerPage-Ready')
