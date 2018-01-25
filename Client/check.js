//Check.js -- checks for db and if not makes one maybe.
const {ipcRenderer} = require('electron') // we do this to send the success message to the renderer.
const remote = require('electron').remote;
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
    //console.log(data)
    //The XML is done Here
    //Add the check online button
    var checkOnline = document.createElement("button");
    checkOnline.innerHTML = "Check Online"

    document.body.appendChild(checkOnline);

    var addOne =  document.createElement("button");
    addOne.innerHTML = "Create One"
    document.body.appendChild(addOne);
    checkOnline.addEventListener("click", checkOnlineF);
    addOne.addEventListener("click", addDb);

    //Add the logout button
    var logoutButton = document.createElement("button");
    logoutButton.innerHTML = 'Logout'
    logoutButton.id = 'logoutButtonId'
    document.getElementById('mainBody').appendChild(logoutButton);
    //Bind the logout button

    logoutButton.addEventListener("click", function(s, xml = null) {
      //i just copied this part ignore the random vars kek
      ipcRenderer.send('logout');
    });
    //Logout button done -- Lets clean up HTML
    document.getElementById('headerMessage').innerHTML = "Here are your on disk athlete databases "
    document.getElementById('details').innerHTML = "If you'd like to check online for more / update your current databases, please click the 'Check Online' button. If you'd like to add a athlete database, click the 'Create One' button! If you'd like to open a specific database, click on its corrisponding name. If it is not there, try updating! "
    //Fill the new buttons of xml sheet
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
          dataText = dataText.replace('/Apache24/htdocs/','')
          //console.log(dataText)
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
            //console.log('Caught the undefined array var, meaning the script has listed all of the buttons');
            break
          }
        }
      loopNum = loopNum + 1;
      } //if closer

    } //while closer

  });

  child2.stdin.write(command + '\n');

}
function checkOnlineF() {
  //global.xmlList = ''

  if (global.xmlList != undefined){
    let dataHolder = ''
    var dataVar = global.xmlList.split(','); // is now a arayy with each file.
    var loopNum = 0;
    var arrayLength = dataVar.length + 1 // So we can do !=, and still have it activate when it =
    while (loopNum != arrayLength) {
      dataHolder = dataVar[loopNum]
      try{
        document.getElementById(dataHolder).remove()
      }
      catch (error){
        //pass
      }
      loopNum = loopNum + 1
    }
}

  //just gonna build it here using the exsisting functions
  var dataCheck = exec("py pythonClient.py ", function (error, stdout, stderr) {
    //console.log('executed');
    if (error !== null) {
      console.log('exec error: ' + error); //Just to catch any errors
    }
  });

  dataCheck.stdout.on('data', function(data) {

    if (data == 1) {
      //If we can't connect to the server
      document.getElementById('headerMessage').innerHTML = 'We could not get a stable connection to the server'
      document.getElementById('details').innerHTML = 'Try checking your connection, then trying again.'
    }
    if (data == 0) {
      // If we connected to the server.
      dataCheck.stdout.end()
      //console.log("we're connected, now trying to get a list of hosted xml files.")
      var xmlCheck = exec("py pythonClient.py ", function (error, stdout, stderr) {
        console.log('executed');
        if (error !== null) {
          console.log('exec error: ' + error); //Just to catch any errors
        }
      });
      //Event for data
      xmlCheck.stdout.on('data', function(data) {

        //handle list of avalible xml sheets
        //console.log(data)
        if (data == 0) {
          document.getElementById('headerMessage').innerHTML = 'Oh no'
          document.getElementById('details').innerHTML = "It seems we are not hosting any files for you! Try uploading a spreadsheet using the 'create one' button, or try again using the 'check online' button!"
          /**
          var checkOnline = document.createElement("button");
          checkOnline.innerHTML = "Check Online"

          document.body.appendChild(checkOnline);

          var addOne =  document.createElement("button");
          addOne.innerHTML = "Create One"
          document.body.appendChild(addOne);
          checkOnline.addEventListener("click", checkOnlineF);
          addOne.addEventListener("click", addDb);
          **/
          //Add the logout button
          var logoutButton = document.createElement("button");
          logoutButton.innerHTML = 'Logout'
          logoutButton.id = 'logoutButtonId'
          document.getElementById('mainBody').appendChild(logoutButton);
          //Bind the logout button

          logoutButton.addEventListener("click", function(s, xml = null) {
            //i just copied this part ignore the random vars kek
            ipcRenderer.send('logout');
          });
        }

        if (data != 0){
          //Delete any pre exsisting buttons
          global.xmlList = data
          document.getElementById('headerMessage').innerHTML = 'Success!'
          document.getElementById('details').innerHTML = "Here are some of your avalible databases that we are hosting. Click on one to download it!"

          //When the stuff actuallu has xml docs in there
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
                dataText = dataText.replace('/Apache24/htdocs/','')
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
                  // Take Y (which is the xml file) and build a new page using i
                  y = y.replace('/Apache24/htdocs/','')
                  console.log(y)
                  var fetchXml = exec("py -i pythonClient.py ", function (error, stdout, stderr) {
                    if (error !== null) {
                      console.log('exec error: ' + error); //Just to catch any errors
                    }
                  });
                  fetchXml.stdout.on('data', function(data) {
                    console.log(data)
                    document.getElementById('headerMessage').innerHTML = 'Loading'
                    document.getElementById('details').innerHTML = "Give us a few while we download your db and put it up!"

                    if (data == 0) {
                      ipcRenderer.send('loginSuccess', 'null') //Reload the page so the new docs show up
                    }
                    if (data != 0) {
                      document.getElementById('headerMessage').innerHTML = 'Oh no'
                      document.getElementById('details').innerHTML = "It seems like we couldn't connect! Try again in a few or restart the program. Do make sure you're connected to the internet!"

                    }
                  });

                  fetchXml.stdin.write('0xGXL$#$'+y+'\n')








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

        }
      });
      xmlCheck.stdin.write('0xG08$#$null'+'\n')
    }
  });
  dataCheck.stdin.write('0xCC0$#$null' + '\n');
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

      document.getElementById('mainBody').appendChild(checkOnline);

      var addOne =  document.createElement("button");
      addOne.innerHTML = "Create One"
      document.getElementById('mainBody').appendChild(addOne);
      var logoutButton = document.createElement("button");
      logoutButton.innerHTML = 'Logout'
      logoutButton.id = 'logoutButtonId'
      document.getElementById('mainBody').appendChild(logoutButton);
      logoutButton.addEventListener("click", function(s, xml = null) {
        //i just copied this part ignore the random vars kek
        ipcRenderer.send('logout');
      });
      checkOnline.addEventListener("click", checkOnlineF);
      addOne.addEventListener("click", addDb);
    }

  });
  child.stdin.write(command+'\n');


}




check();
