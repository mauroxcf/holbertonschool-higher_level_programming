#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    for (let height = 0; height < this.height; height++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
