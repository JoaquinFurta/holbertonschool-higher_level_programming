#!/usr/bin/node
// Reads a file and prints it

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data);
});
