#!/usr/bin/node
let num1 = parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log(1);
} else {
  let retNum = 1;
  for (; num1 > 0; num1--) {
    retNum *= num1;
  }
  console.log(retNum);
}
