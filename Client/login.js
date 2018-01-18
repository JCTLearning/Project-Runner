//Login script -- Quick question: Why do some lines need ; and others dont?!?!
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;
function checkData(data, userData){
  /*
  User data is username:pass
  I had to convert true//false values into ones or zeros because JS wasn't reading string values correctly... We need a fix for that.
  */
  //console.log('Call was passed correctly') --  TO check if I did the function correctly
  //console.log(data)
  var pythonData = Number(data); //Either 0 or 1 // true or false

  if(pythonData == 0){
    ipcRenderer.send('loginSuccess', userData); //Switches our prog over to the main script
    console.log('Changing Page...');
  }
  if(pythonData == 1) {
    console.log('Failed')
    document.getElementById('erroCont').innerHTML = 'Login Failed, Check your username or password!'
  }
}
function login(){
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value
  //console.log(username)
  //console.log(password)
  var pyString = '0xL0S$#$' + username + '!' + password //0xL0S$#$username:password
  var userData = username + '!' + password
  //console.log(pyString)
  //Now we pass that on to python.
  var child = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });

  child.stdout.on('data', function(data) {
    var returnResult = data.toString();

    console.log('Returned Result: '+ returnResult);

    checkData(returnResult, userData)

  });
  child.stdin.write(pyString+'\n'); //Now the thing is \n is equivelant (exuse meh spelling, you get the point) to putting enter. stdin needs that enter in order to proc the command.
  //Well my orginal plan was to process the data here but with that event above I cant sooooo oh well :shrug:


}


document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("loginButton").addEventListener("click", login);

})
