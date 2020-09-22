#!/usr/bin/node
const req = require('request');
const fs = require('fs');

const theUrl = process.argv[2];
const file = process.argv[3];

req.get({ url: theUrl }, function (err, res, body) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    // const json = JSON.parse(body);
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
