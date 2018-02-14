//data.js
const {ipcRenderer} = require('electron');
var sys = require('sys');
var exec = require('child_process').exec;
const {shell} = require('electron')



function main(row) {
  console.log('started')

  var time = document.getElementById('time').value

  var pyString =  row+'#'+time
  console.log(pyString)
  var child = exec("pythonClient.exe");
  child.stdout.on('data', function(data) {
    //create Main div
    check = parseInt(data)
    if(check == 0) {
      document.getElementById('mainText').innerHTML = 'You did not enter a value correctly'
    }
    else {
      document.getElementById('buttons').remove()
      document.getElementById('time').remove()
      document.getElementById('mainText').innerHTML = "VDOT: " + data;
      var restartB = document.createElement('button');
      restartB.id = 'restartB'
      restartB.innerHTML = 'Restart'
      document.getElementById('bodyText').appendChild(restartB)
      document.getElementById('restartB').addEventListener('click', function(){
      ipcRenderer.send('restart')
      });
    }

   });
   child.stdin.write(pyString + "\n")



}
document.addEventListener('DOMContentLoaded', function() {

  document.getElementById('minMize').addEventListener('click', function(){ipcRenderer.send('min');});
  document.getElementById('maxMize').addEventListener('click', function(){ipcRenderer.send('max');});
  document.getElementById('exitButton').addEventListener('click', function(){ipcRenderer.send('close');});
  document.getElementById('1500').addEventListener('click', function(){main('1')});
  document.getElementById('1600').addEventListener('click', function(){ main('2')});
  document.getElementById('3000').addEventListener('click', function(){main('4')});
  document.getElementById('3200').addEventListener('click', function(){main('5')});
  document.getElementById('mile').addEventListener('click', function(){main('3')});
  document.getElementById('mile2').addEventListener('click', function(){main('6')});

});
