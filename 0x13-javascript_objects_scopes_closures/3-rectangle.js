#!/usr/bin/node
module.exports = class Rectangle {
  constructor (x, h) {
    if (x > 0 && h > 0) {
      this.width = x;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const array = [];
      for (let j = 0; j < this.width; j++) {
        array.push('X');
      }
      console.log(array.join(''));
    }
  }
};
