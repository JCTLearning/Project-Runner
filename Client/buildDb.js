// buildDb.js
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;
function buildSpreadsheet() {
  var userSpreadsheet = document.getElementById('spreadsheetUrl').value
  var teamName = document.getElementById('teamName').value
  document.getElementById('teamName').remove()
  document.getElementById('spreadsheetUrl').remove()
  document.getElementById('spreadsheetButton').remove()
  var pyString = "0xL08$#$"+teamName+"_@#@_" + userSpreadsheet //0xL08$#$john_@#@_https://docs.google.com/d/examplespreadsheet
  var child = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });

  child.stdout.on('data', function(data) {


    var returnResult = data.toString();
    document.getElementById('headerMessage').innerHTML = "Success"
    document.getElementById('details').innerHTML = "Please wait while we download the file!";
    if (returnResult == 0) {
      //If Succeeded
      pyString2 = "0xGXL$#$"+returnResult
      //console.log(pyString2)
      var child2 = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
        if (error !== null) {

          console.log('exec error: ' + error); //Just to catch any errors
        }
      });
      child2.stdout.on('data', function(data) {
        Data = parseInt(data)
        if (data == '0') {
          //success
          ipcRenderer.send('returnResult', 'null') //Since it was a success we reload the page so we may find the downloaded spreadsheet
        }
        if (data == '1') {
          // Fail
          document.getElementById('headerMessage').innerHTML = "Download Failed"
          document.getElementById('details').innerHTML = "Please check your internet connection and restart the program...";
        }
      });
      child2.stdin.write(pyString2+'\n');
    }
    if (returnResult != 0) {
      //If Failed
      document.getElementById('details').innerHTML = "There was a failure in our process. Check your internet connection and make sure the spreadsheet is shared with projectrunner-test@pr-testingdata.iam.gserviceaccount.com";
      document.getElementById('headerMessage').innerHTML = "Failure"
      }




  });

  child.stdin.write(pyString+'\n');
}

/* Lets bind the main button :P */
document.addEventListener('DOMContentLoaded', function() {
  var backButton = document.createElement("button");
  backButton.innerHTML = 'Back'
  backButton.id = 'backButtonId'
  backButton.className = 'sysButton'
  document.getElementById('mainBody').appendChild(backButton);
  //Bind the back button

  backButton.addEventListener("click", function(s, xml = null) {
    //console.log('Bounded');// -- making sure this function is running.
    ipcRenderer.send('loginSuccess');
  });
  document.getElementById("spreadsheetButton").addEventListener("click", function() {

    document.getElementById('headerMessage').innerHTML = "Please Wait"
    document.getElementById('details').innerHTML = "This could take awhile so please don't close the program!";
    buildSpreadsheet();
  });

})
