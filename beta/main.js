//main.jS
const electron = require('electron')
const app = electron.app
const {ipcRenderer} = require('electron')
const {ipcMain} = require('electron')
const BrowserWindow = electron.BrowserWindow
const path = require('path')
//Main window establisj
var mainWindow = null
const createWindow = () => {
  mainWindow = new BrowserWindow({width: 3000, height: 1000, darkTheme: true})
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'main.html'), //Our main login Page
    protocol: 'file:',
    slashes: true
  }))
  mainWindow.on('closed', () => {
    mainWindow = null
    })
}

ipcMain.on('restart', function(){
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'main.html'), //Our main html Page
    protocol: 'file:',
    slashes: true
  }));
})
//Start of app
app.on('ready', createWindow)
app.on('window-all-closed', () => {
  if(process.platform !== 'darwin') {
    app.quit()
  }
})
app.on('activate', () => {
  if(mainWindow === null){
    createWindow()
  }
})
