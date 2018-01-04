//Check.js -- checks for db and if not makes one maybe.
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
var sys = require('sys'); //Need these for later.
var exec = require('child_process').exec;

function getSSData() {
  var command = '0xL0B$#$null'
  // Here we cd to the folder and search for xml clients
  document.getElementById('headerMessage').innerHTML = "Files found!"
  document.getElementById('details').innerHTML = "Give us a few while we load them in!"
  //load xml titles and bind buttons to them etc etc etc
  var child2 = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
    console.log('executed')
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });
  child2.stdout.on('data', function(data) {
    console.log(data)
    /*
    Here comes the problem here, we need to create a list of buttons, yet we dont have a var for each
    */
    let dataHolder = ''
    var dataVar = data.split(','); // is now a arayy with each file.
    var loopNum = 0;
    var arrayLength = dataVar.length + 1 // So we can do !=, and still have it activate when it =
    while (loopNum != arrayLength) {
      dataHolder = dataVar[loopNum]
      //IF not underfined build webpage
      if (dataHolder !== null) {
        try{
          var dataText = dataHolder.replace('.xml', '');
          var button =  document.createElement("button");
          button.innerHTML = dataText
          button.id = dataHolder

          document.body.appendChild(button);
          /*
          AHAHAHHAAHAHAHA THAT WAS A GUESS I DIDNT THINK DEFINING A VAR IN THE FUNCTION CALL WOULD CARRY THE DATA INTO THE FUNCTION LMAO
          Anyways, there's a problem. No matter what button.id will = 'deleted' because its pulling the last version of button id,
          which is the deleted one below sooooooo we need to fix that.
          */
          //eval("refrenceTag_" +dataHolder +"= dataHolder");
          var x = "refrenceTag_" + dataHolder

          button.addEventListener('click',  function(s, y = this.id) {
            // Take Y (which is the xml file) and build a new page using is
            ipcRenderer.send('buildRunnerPage', y)
          });
        }
        catch (error) {
          if (error.name === 'TypeError') {
            button.id = "delete" //yes yes yes we could just combine two lines, but im lazy.
            document.getElementById("delete").remove();//delete the element, so we don't get an empty button
            console.log('Caught the undefined array var, meaning the script has listed all of the buttons');
            break
          }
        }
      loopNum = loopNum + 1;
      } //if closer

    } //while closer

  });

  child2.stdin.write(command + '\n');

}
function checkOnlineF(evt) {
  console.log("Checking Online");
}

function addDb() {
  console.log('Changing pages -- Build DB off of Spreadsheet page');
  var emptyVar = null;
  ipcRenderer.send('buildDb', emptyVar);
}
function check() {
  var command = '0xCD8$#$null' //I don't wanna build an entire function in the client to catch if its a db check, so i included the $#$, basically im lazy and this could be done better
  var child = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });
  child.stdout.on('data', function(data) {
    var returnResult = data.toString();
    console.log(returnResult)
    returnResult = Number(returnResult) //Convert to a number, because string stuff is being weird, see login.js for details.
    if(returnResult == 0) {
      child.stdin.end(); //we need to end the previous command
      getSSData();
    }
    if(returnResult == 1) {
      document.getElementById('headerMessage').innerHTML = "Couldn't Find anythin' :C"
      document.getElementById('details').innerHTML = "we couldn't find any data on the local disk, would you like to check online or add one?"
      var checkOnline = document.createElement("button");
      checkOnline.innerHTML = "Check Online"

      document.body.appendChild(checkOnline);

      var addOne =  document.createElement("button");
      addOne.innerHTML = "Create One"
      document.body.appendChild(addOne);
      checkOnline.addEventListener("click", checkOnlineF());
      addOne.addEventListener("click", addDb);
    }

  });
  child.stdin.write(command+'\n');


}




check();
