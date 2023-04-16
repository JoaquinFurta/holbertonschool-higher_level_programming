#!/usr/bin/node
/* define a class Recatngle */

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w === 0 || w <= 0 || h === 0 || h <= 0) && (w && h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log('X'.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
  }
};
