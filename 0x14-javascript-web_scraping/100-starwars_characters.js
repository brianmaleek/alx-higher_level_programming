#!/usr/bin/node

/**
 * Script prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 * You must use the Star wars API
 * You must use the module request
 */

const request = require('request');

// Check if argument is passed
if (process.argv.length < 3) {
  console.log('Usage: ./100-starwars_characters.js <filmId>');
  process.exit(1);
}

// Get movie id and API url
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make request to API
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
        } else if (res.statusCode !== 200) {
          console.log('Invalid URL');
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
