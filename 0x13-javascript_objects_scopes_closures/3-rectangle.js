#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let height = 0; height < h; height++) {
          console.log('X'.repeat(w));
        }
      }
    } else {
      {}
    }
  }
}
module.exports = Rectangle;
