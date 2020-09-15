#!/usr/bin/node
/* prints based on number of given arguments to script */
// const process = require('process');
// that line is not strictly neccesary
// var args = process.argv;
// console.log(args.length)
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
