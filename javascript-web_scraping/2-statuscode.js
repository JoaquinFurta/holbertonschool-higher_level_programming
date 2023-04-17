#!/usr/bin/node

const process = require('process');
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  console.log(`code: ${response.statusCode}`);
});
