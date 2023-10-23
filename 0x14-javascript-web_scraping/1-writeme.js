#!/usr/bin/node

/**
 * Script writes a string to a file.
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */

const fs = require('fs');

// Check if file path and content to write are provided
if (process.argv.length < 4) {
  console.log('Usage: node 1-writeme.js <file path> <content to write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write content to file in utf-8 format
fs.writeFile(filePath, contentToWrite, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
