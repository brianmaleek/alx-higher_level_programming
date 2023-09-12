#!/usr/bin/node

// class Rectangle that defines a rectangle
// initializes: w: width, h: height
// if w or h is equal to 0 or not a positive integer, create an empty object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // empty object
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
// module.exports exports the class Rectangle
module.exports = Rectangle;
