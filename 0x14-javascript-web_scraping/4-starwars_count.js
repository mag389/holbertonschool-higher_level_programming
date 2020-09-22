#!/usr/bin/node
const req = require('request');
// const RegExp = require('regex');
const theUrl = process.argv[2];
// const personurl = 'https://swapi-api.hbtn.io/api/people/18';

// theUrl = theUrl + process.argv[2];
req.get({ url: theUrl }, function (err, res, body) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    const json = JSON.parse(body);
    let numfilms = 0;
    for (const film of json.results) {
      for (const character of film.characters) {
        // console.log(character);
        if (character.includes('18')) {
          numfilms += 1;
        }
      }
    }
    console.log(numfilms);
  }
});
