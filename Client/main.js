// Main Electron Prog
const electron = require('electron')
const app = electron.app
const {ipcRenderer} = require('electron')
const {ipcMain} = require('electron')
const BrowserWindow = electron.BrowserWindow
const path = require('path')


/* [-- Some issues as of now --]
  --Python is supposed to return a string back to java script. It is but its not able to be read by any if statements. For example...:
    `
    var pythonData = data.toString(); //Convert it into a string
    if (pythonData == "True"){
      runFunct();
  }
    `
    The problem is `pythonData` even if the string inside is "True", never equals "True" in an if statement.
    The fix to that is converting all True//False statements into a 0//1 statement and using Number() to convert to an int.
  [-- Other notes --]
    If you want you can fix my `.loadURL(require('URL').format)` to something else to where we aren't requiring it everytime.
    We should reorganize each page into its own folder kek
*/


let mainWindow = null // Global window var
let userData = null // I wanna pass the user info from window to window so ima make it global
let xmlSheet = null // I want this to be global so we can acess it in the other events
let runnerIdVar = null //Need this for creating indv runner pages
const createLogin = () => {
  mainWindow = new BrowserWindow({width: 1000, height: 600})
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'login.html'), //Our main login Page
    protocol: 'file:',
    slashes: true
  }))
  mainWindow.on('closed', () => {
    mainWindow = null
    })
    //end of login funct
}
// Login
ipcMain.on('loginSuccess', (event, userData) => {
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'handleDb.html'), //Our main html Page
    protocol: 'file:',
    slashes: true
  }))

});

// Make a data base off of a google spreadsheet
ipcMain.on('buildDb', (event, emptyVar) => {
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'buildDb.html'), //Our main html Page
    protocol: 'file:',
    slashes: true
  }))

});
// Display a data base
ipcMain.on('buildRunnerPage', (event, xmlSheets) => {
  //console.log(xmlSheet); -- Confirmimng if the var is full
  xmlSheet = xmlSheets //Putting it in the global var
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'buildRunnerPage.html'), //Our main html Page
    protocol: 'file:',
    slashes: true
  }))

});
ipcMain.on('buildRunnerPage-Ready', (event) => {
  event.sender.send('buildDb', xmlSheet); //We create a new listener so we can send it using "event". IF we call it in buildRunnerPage it'll send it to the wrong render window.
});
ipcMain.on('buildIndvPage', (event, runnerId) => {
  runnerIdVar = runnerId
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'buildIndvPage.html'), //Our main html Page
    protocol: 'file:',
    slashes: true
  }))

});
ipcMain.on('buildIndvPage-Ready', (event) => {
  event.sender.send('continue', runnerIdVar, xmlSheet)
})
app.on('ready', createLogin)
app.on('window-all-closed', () => {
  if(process.platform !== 'darwin') {
    app.quit()
  }
})
app.on('activate', () => {
  if(mainWindow === null){
    createLogin()
  }
})
