#!/usr/bin/node

/**
 * Script gets contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 * You must use the module request
 */

const request = require('request');
const fs = require('fs');

// Check if URL and file path are provided
if (process.argv.length < 4) {
  console.log('Usage: node 5-request_store.js <URL> <file path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make GET request to URL
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Invalid URL');
  } else {
    // Write body response to file in utf-8 format
    fs.writeFile(filePath, body, 'utf-8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
