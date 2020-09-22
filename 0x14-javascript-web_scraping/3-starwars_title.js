#!/usr/bin/node
const req = require('request');
const theUrl = 'https://swapi-api.hbtn.io/api/films/';

req.get({ url: theUrl + process.argv[2] }, function (err, res, body) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
