#!/usr/bin/node
const req = require('request');
// let theUrl = 'https://swapi-api.hbtn.io/api/films/';
const personurl = 'https://swapi-api.hbtn.io/api/people/18';

// theUrl = theUrl + process.argv[2];
req.get({ url: personurl }, function (err, res, body) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    const json = JSON.parse(body);
    console.log(json.films.length);
  }
});
