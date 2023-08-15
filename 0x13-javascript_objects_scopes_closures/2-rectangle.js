#!/usr/bin/node
module.exports = class Rectangle {
  constructor (x, h) {
    if (x > 0 && h > 0) {
      this.width = x;
      this.height = h;
    }
  }
};
