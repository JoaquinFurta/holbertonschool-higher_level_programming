#!/usr/bin/node
/* basic script */

const process = require('process');

const argLen = process.argv.length;

if (argLen === 3) {
  console.log('Argument found');
} else if (argLen > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
