#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      console.log(c.repeat(this.width).concat('\n').repeat(this.width).slice(0, -1));
    }
  }
};
