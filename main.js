'use strict';
const {app, BrowserWindow} = require('electron');
const $ = require('jquery');

const url = require('url')
const path = require('path')
try {
	require('electron-reload')(__dirname);
} catch (err) {}
let win

function createWindow() {
   win = new BrowserWindow({width: 800, height: 600, frame: true})
   win.loadURL('http://localhost:3000/');
}

app.on('ready', createWindow)