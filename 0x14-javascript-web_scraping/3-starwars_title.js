#!/usr/bin/node

/**
 * Script prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 * You must use the module request
 */

const request = require('request');

// Check if movie ID is provided
if (process.argv.length < 3) {
  console.log('Usage: node 3-starwars_title.js <movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make GET request to the Star wars API endpoint
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Invalid movie ID');
  } else {
    console.log(JSON.parse(body).title);
  }
});
