#!/usr/bin/node

/**
 * Script to print all characters of a specified Star Wars movie.
 *
 * Usage: ./0-starwars_characters.js <movie_id>
 *
 * This script takes a single command-line argument, the movie ID, and retrieves
 * all character names for that movie from the Star Wars API (https://swapi.dev).
 * The character names are printed in the order they appear in the API's character list.
 *
 * Example:
 * ./0-starwars_characters.js 3
 * Output:
 * Luke Skywalker
 * C-3PO
 * R2-D2
 * Darth Vader
 * ...
 *
 * Dependencies:
 * - request (install with `npm install request`)
 *
 * Environment:
 * - Node.js runtime is required.
 */

const request = require('request');
const API_URL = 'https://swapi.dev/api';

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Function to fetch and display the characters of the specified movie
function getStarWarsCharacters (movieId) {
  const movieUrl = `${API_URL}/films/${movieId}/`;

  request(movieUrl, (err, _, body) => {
    if (err) {
      console.error('Error fetching movie:', err);
      return;
    }

    let movieData;
    try {
      movieData = JSON.parse(body);
    } catch (parseErr) {
      console.error('Error parsing movie data:', parseErr);
      return;
    }

    // Fetch each character's name in order
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, (charErr, __, charBody) => {
        if (charErr) {
          console.error('Error fetching character:', charErr);
          return;
        }

        let characterData;
        try {
          characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } catch (charParseErr) {
          console.error('Error parsing character data:', charParseErr);
        }
      });
    });
  });
}

// Call the function to fetch and display the characters
getStarWarsCharacters(movieId);
