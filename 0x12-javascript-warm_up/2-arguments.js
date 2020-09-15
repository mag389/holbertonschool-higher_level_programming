#!/usr/bin/node
// const process = require('process');
// var args = process.argv;
// console.log(args.length)
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
