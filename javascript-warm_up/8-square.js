#!/usr/bin/node
/* basic script */
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(Array(parseInt(process.argv[2])).fill('X').join(''));
  }
}
