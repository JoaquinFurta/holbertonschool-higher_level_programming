#!/usr/bin/node
/* script to calculate a factorial of a number */
const process = require('process');

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
