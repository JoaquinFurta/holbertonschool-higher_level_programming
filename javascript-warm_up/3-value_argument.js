#!/usr/bin/node
/* basic script */

const process = require('process');

let argLen = 0;

process.argv.forEach(function (elem) {
  argLen++;
});

if (argLen === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
