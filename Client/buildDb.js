// buildDb.js
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;
function buildSpreadsheet() {
  var userSpreadsheet = document.getElementById('spreadsheetUrl').value
  var teamName = document.getElementById('teamName').value
  var pyString = "0xL08$#$"+teamName+"_@#@_" + userSpreadsheet //0xL08$#$john_@#@_https://docs.google.com/d/examplespreadsheet
  var child = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });

  child.stdout.on('data', function(data) {
    var returnResult = data.toString();
    document.getElementById('erroCont').innerHTML = returnResult;

  });

  child.stdin.write(pyString+'\n');
}

/* Lets bind the main button :P */
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("spreadsheetButton").addEventListener("click", buildSpreadsheet);

})
