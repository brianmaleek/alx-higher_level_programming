#!/usr/bin/node

let numArgumentsPrinted = 0;

// Function that prints the number of arguments already
// printed and the new argument value
exports.logMe = function (item) {
  console.log(numArgumentsPrinted + ': ' + item);
  numArgumentsPrinted++;
};
