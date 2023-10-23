#!/usr/bin/node

/**
 * Script displays the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */

const request = require('request');

// Check if URL is provided
if (process.argv.length < 3) {
  console.log('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Make GET request to URL
request(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
