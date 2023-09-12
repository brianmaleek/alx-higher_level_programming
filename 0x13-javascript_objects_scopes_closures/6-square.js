#!/usr/bin/node

// class square that defines a square and
// inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle');

// class Square inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // method print() prints the rectangle using the character c
  // if c is undefined, use the character X

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

// module.exports exports the class Square
module.exports = Square;
