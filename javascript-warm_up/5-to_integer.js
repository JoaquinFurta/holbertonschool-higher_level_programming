#!/usr/bin/node
/* basic script */

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + process.argv[2]);
}
