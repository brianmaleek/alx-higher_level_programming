#!/usr/bin/node

// Import the list from 100-data.js
const list = require('./100-data').list;

// Create a new list with the values multiplied by their index
const newlist = list.map((value, index) => value * index);

// Print the original list and the new list
console.log(list);
console.log(newlist);
