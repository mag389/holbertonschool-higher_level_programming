#!/usr/bin/node
const req = require('request');
const theUrl = process.argv[2];

req.get({ url: theUrl }, function (err, res) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
