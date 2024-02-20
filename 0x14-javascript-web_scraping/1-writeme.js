#!/usr/bin/node
// Import the fs and process modules
const fs = require('fs');
const process = require('process');

// Get the file path and the string to write from the arguments
const filePath = process.argv[2];
const data = process.argv[3];

// Write the file using the writeFile method
fs.writeFile(filePath, data, 'utf-8', (error) => {
  // If an error occurred, print the error object
  if (error) {
    console.error(error);
  }
});
