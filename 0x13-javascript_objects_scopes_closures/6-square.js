#!/usr/bin/node
const PSquare = require('./5-square');
class Square extends PSquare {
  charPrint (c) {
    if (c === null || c === undefined) {
      c = 'X';
    }
    let x = c;
    for (let i = 1; i < parseInt(this.width); i++) {
      x = x + c;
    }
    for (let i = 0; i < parseInt(this.height); i++) {
      console.log(x);
    }
  }
}
module.exports = Square;
