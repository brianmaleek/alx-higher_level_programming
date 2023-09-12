#!/usr/bin/node

// class square that defines a square and inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle');

// class Square inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

// module.exports exports the class Square
module.exports = Square;
