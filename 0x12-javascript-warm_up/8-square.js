#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let x = 'X';
  for (let i = 1; i < parseInt(process.argv[2]); i++) {
    x = x + 'X';
  }
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(x);
  }
}
