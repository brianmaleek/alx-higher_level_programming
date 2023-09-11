#!/usr/bin/node

// converts the first two arguments passed to the script to integers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// function that returns the addition of 2 integers
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return a + b;
  }
}
console.log(add(a, b));
