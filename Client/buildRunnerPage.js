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
  document.getElementById('headerTitle').innerHTML = "Current DB: "+xmlName
  //Create the button divs
  mainDiv = document.createElement('div');
  mainDiv.id = 'runnerData'
  document.getElementById('mainBody').appendChild(mainDiv)

  headerMessage = document.createElement('h')
  headerMessage.innerHTML = "Here are your Avalible Runners"
  headerMessage.className = "message"
  document.getElementById('runnerData').appendChild(headerMessage)

  buttonDiv = document.createElement('div');
  buttonDiv.id = 'runnerButton'
  document.getElementById('runnerData').appendChild(buttonDiv)

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
    //console.log(runnerData[loopNum]); --  For testing
    x = runnerData[loopNum];
    runnerDiv = document.createElement('div')
    runnerDiv.id = x.getAttribute("name")
    document.getElementById('runnerButton').appendChild(runnerDiv)
    runnerName = x.getAttribute("name");
    runnerId = x.getAttribute("id")
    var button =  document.createElement("button");
    button.innerHTML =  runnerName + " Details" //I guess we can put the adv vdot here. Then design each button :P
    button.id = runnerId
    button.className = "button";

    document.getElementById(x.getAttribute("name")).appendChild(button);
    button.addEventListener('click',  function(s, y = this.id) {
      // Take Y (which is the xml file) and build a new page using is
      ipcRenderer.send('buildIndvPage', y)
    });
    // End of loop
    loopNum = loopNum +  1

  }
  //BackButton
  var sysButtonsDir = document.createElement('div')
  sysButtonsDir.id = 'sysButtonsDir'
  document.getElementById('mainBody').appendChild(sysButtonsDir)
  var backButton = document.createElement('button');
  backButton.id = 'backButtonId'
  backButton.innerHTML = 'Back'
  backButton.className = 'sysButton'
  document.getElementById('sysButtonsDir').appendChild(backButton);
  backButton.addEventListener('click', function(x, emptyVar = null) {
    ipcRenderer.send('loginSuccess'); //truth be told id why im just taking up ram space here, guess I dont wanna create a whole entire function :shrug:
    //Also yes i know "login success" isnt a descriptive var, but im not creating two ipcrender funcs that do the same bloody thing.
  });
  //LogoutButton
  var logoutButton = document.createElement("button");
  logoutButton.innerHTML = 'Logout'
  logoutButton.id = 'logoutButtonId'
  logoutButton.className = "sysButton"
  document.getElementById('sysButtonsDir').appendChild(logoutButton);
  //Bind the logout button

  logoutButton.addEventListener("click", function(s, xml = null) {
    //i just copied this part ignore the random vars kek
    ipcRenderer.send('logout');
  });


  }
ipcRenderer.send('buildRunnerPage-Ready')
