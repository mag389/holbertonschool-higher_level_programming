#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
console.log(fact(num1));
function fact (num1) {
  if (isNaN(num1)) {
    return 1;
  } else if (num1 === 1) {
    return 1;
  } else {
    return (num1 * fact(num1 - 1));
  }
}
