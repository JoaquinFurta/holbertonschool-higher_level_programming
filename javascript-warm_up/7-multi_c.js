#!/usr/bin/node
/* basic script */
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('c is fun');
  }
}
