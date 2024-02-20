#!/usr/bin/node
// Import the request, fs, and process modules
const request = require('request');
const fs = require('fs');
const process = require('process');

// Get the URL to request and the file path to store from the arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Create a writable stream to the file using the fs module
const fileStream = fs.createWriteStream(filePath, 'utf-8');

// Make a GET request using the request method and pipe the data to the file stream
request.get(url).pipe(fileStream);
