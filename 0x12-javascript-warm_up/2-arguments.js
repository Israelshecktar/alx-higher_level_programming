#!/usr/bin/node
// A script that prints a message depending on the number of arguments

const args = process.argv[2];
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
