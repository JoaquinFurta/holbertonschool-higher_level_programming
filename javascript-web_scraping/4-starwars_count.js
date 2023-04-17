#!/usr/bin/node

const process = require('process');
const request = require('request');

let count = 0;
request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  const films = JSON.parse(body);

  films.results.forEach((elem) => {
    elem.characters.forEach((pj) => {
      if (pj.slice(-3, -1) === '18') {
        count++;
      }
    });
  });
  console.log(count);
});
