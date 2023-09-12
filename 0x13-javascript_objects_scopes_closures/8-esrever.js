#!/usr/bin/node

// Function that reverses a list
exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversedList = [];
  // Loop through the list backwards
  for (let i = list.length - 1; i >= 0; i--) {
    // Add the current element to the reversed list
    reversedList.push(list[i]);
  }
  // Return the reversed list
  return reversedList;
};
