#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  console.log(body);
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
