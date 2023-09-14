#!/usr/bin/node

// Import the fs module
const fs = require('fs');

// Read the contents of the first file
const sourceFile1 = fs.readFileSync(process.argv[2], 'utf8');
// Read the contents of the second file
const sourceFile2 = fs.readFileSync(process.argv[3], 'utf8');
// Write the concatenation of the two files to the third file
fs.writeFileSync(process.argv[4], sourceFile1 + sourceFile2, 'utf8');
