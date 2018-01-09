// checkXmlOnline.js -- checks online for new xml sheets and updates them

const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;
/**
  actually I just wanna updat e


function main() {
  //First set up html data
  document.getElementById('headerMessage').innerHTML = 'Establising connection'
  document.getElementById('details').innerHTML = 'Getting a stable connection to the Project Runner Server...'
  //Fetch XML Sheet list
}
