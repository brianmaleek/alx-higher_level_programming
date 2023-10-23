#!/usr/bin/node

/**
 * Script prints the number of movies where the character “Wedge Antilles” is present.
 * The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 * You must use the module request
 */

const request = require('request');

// Check if movie ID is provided
if (process.argv.length < 3) {
  console.log('Usage: node 4-starwars_count.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

// Make GET request to the Star wars API endpoint
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Invalid movie ID');
  } else {
    const data = JSON.parse(body).results;
    const moviesWithWedgeAntilles = data.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log(moviesWithWedgeAntilles.length);
  }
});
