#!/usr/bin/node
// a script that displays status code

const request = require('request');
const process = require('process');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
