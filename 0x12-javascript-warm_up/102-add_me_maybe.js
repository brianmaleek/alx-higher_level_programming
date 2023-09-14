#!/usr/bin/n

// This function increments and calls the function passed to it.
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}
module.exports.addMeMaybe = addMeMaybe;
