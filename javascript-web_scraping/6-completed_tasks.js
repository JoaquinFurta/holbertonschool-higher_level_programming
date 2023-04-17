#!/usr/bin/node

const process = require('process');
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  let count = 0;
  const res = {};
  const obj = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    obj.forEach((elem) => {
      if (elem.completed === true && i === elem.userId) count++;
    });
    res[i] = count;
    count = 0;
  }
  console.log(res);
});
