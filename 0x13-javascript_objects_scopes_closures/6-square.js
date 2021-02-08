#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let height = 0; height < this.size; height++) {
      if (c == undefined) {
        console.log('X'.repeat(this.size));
      } else {
        console.log('C'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
