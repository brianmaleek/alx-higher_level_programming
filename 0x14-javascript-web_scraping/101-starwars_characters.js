#!/usr/bin/node

/**
 * Script prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of the list “characters” in the /films/ response
 * You must use the Star wars API
 * You must use the module request
 */

const request = require('request');

// Check if argument is passed
if (process.argv.length < 3) {
  console.log('Usage: ./101-starwars_characters.js <film_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Invalid URL');
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    function displayCharacterName (index) {
      if (index >= characters.length) {
        return;
      }
      request(characters[index], (err, res, body) => {
        if (err) {
          console.log(err);
        } else if (res.statusCode !== 200) {
          console.log('Invalid URL');
        } else {
          console.log(JSON.parse(body).name);
        }
        displayCharacterName(index + 1);
      });
    }
    // display character name
    displayCharacterName(0);
  }
});
