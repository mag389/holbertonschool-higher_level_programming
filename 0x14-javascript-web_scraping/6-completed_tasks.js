#!/usr/bin/node
const req = require('request');

const theUrl = process.argv[2];

req.get({ url: theUrl }, function (err, res, body) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    const json = JSON.parse(body);
    const numtasks = {};
    for (const tasks of json) {
      if (tasks.completed === false) {
        continue;
      }
      if (numtasks[tasks.userId] === undefined) {
        numtasks[tasks.userId] = 1;
      } else {
        numtasks[tasks.userId] += 1;
      }
    }
    console.log(numtasks);
  }
});
