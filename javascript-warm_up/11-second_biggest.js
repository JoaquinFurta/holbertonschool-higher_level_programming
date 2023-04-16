#!/usr/bin/node
/* script that returns the second biggest integer in the list of arguments */
const process = require('process');

if (!process.argv[4]) {
  console.log('0');
} else {
  process.argv.splice(0, 2);
  const array = process.argv.map(elem => parseInt(elem));
  console.log(Math.max(...array.filter(elem => elem !== Math.max(...array))));
}
