#!/usr/bin/node
// script that computes and prints a factorial

const n = +process.argv[2];
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log('The factorial of ' + n + ' is ' + factorial(n));
