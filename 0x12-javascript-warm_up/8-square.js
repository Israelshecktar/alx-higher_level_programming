#!/usr/bin/node
// script that prints a square

const size = +process.argv[2];
if (typeof size === 'number' && !isNaN(size) && size > 0 && size === Math.floor(size)) {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
