#!/usr/bin/node
let num1 = parseInt(process.argv[2]);
let num2 = parseInt(process.argv[3]);
if (isNaN(num1)) {
  console.log(0);
} else if (isNaN(num2)) {
  console.log(0);
} else {
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > num1) {
      num2 = num1;
      num1 = process.argv[i];
    } else if (process.argv[i] > num2) {
      num2 = process.argv[i];
    }
  }
  console.log(num2);
}
