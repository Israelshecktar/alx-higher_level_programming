#!/usr/bin/node
// A script that prints a message depending on the number of arguments

let args = process.argv.length - 2;
if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
