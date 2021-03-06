#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!parseInt(w) || !parseInt(h)) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let x = 'X';
    for (let i = 1; i < parseInt(this.width); i++) {
      x = x + 'X';
    }
    for (let i = 0; i < parseInt(this.height); i++) {
      console.log(x);
    }
  }
}
module.exports = Rectangle;
