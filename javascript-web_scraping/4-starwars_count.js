#!/usr/bin/node

const process = require('process');
const request = require('request');

process.argv[2] = 'https://swapi-api.hbtn.io/api/people/18';
request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).films.length);
});
