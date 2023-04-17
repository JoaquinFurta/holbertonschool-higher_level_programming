#!/usr/bin/node

const process = require('process');
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  let count = 0;
  const res = {};
  const obj = JSON.parse(body);
  try {
    let i = 0;
    while (1) {
      obj.forEach((elem) => {
        if (elem.completed === true && obj[i].userId === elem.userId) count++;
      });
      if (count !== 0) res[obj[i].userId] = count;
      count = 0;
      i++;
    }
  } catch (e) {
    console.log(res);
  }
});