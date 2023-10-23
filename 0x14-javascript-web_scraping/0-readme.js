#!/usr/bin/node

/**
 * Script reads and prints content of a file
 * First argument is the file path
 * Content is read in utf-8 format
 * If an error occurs during reading, prints error object
 */

const fs = require('fs');

// Check if file path is provided
if (process.argv.length < 3) {
  console.log('Usage: node 0-readme.js <file path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read file in utf-8 format
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
