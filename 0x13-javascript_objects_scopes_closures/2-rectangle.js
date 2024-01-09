#!/usr/bin/node
// A class rectangle wth constructor

class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0 || isNaN(w) || isNaN(h)) {
      this.width = w;
      this.heigth = h;
    } else {
      return {};
    }
  }
}
module.exports = Rectangle;
