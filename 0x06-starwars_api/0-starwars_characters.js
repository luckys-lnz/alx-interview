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
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a movie ID is provided as a command-line argument
if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const movieUrl = `${API_URL}/films/${movieId}/`;

  /**
   * Fetches movie data based on movie ID, then fetches and prints each character's name.
   */
  request(movieUrl, (err, _, body) => {
    if (err) return console.error('Error fetching movie:', err);

    let characters;
    try {
      // Parse the response body to access the characters list
      characters = JSON.parse(body).characters;
    } catch (parseErr) {
      return console.error('Error parsing movie data:', parseErr);
    }

    // Map character URLs to promises that resolve to character names
    const characterPromises = characters.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (charErr, __, charBody) => {
            if (charErr) reject(charErr);
            else {
              try {
                resolve(JSON.parse(charBody).name);
              } catch (charParseErr) {
                reject(charParseErr);
              }
            }
          });
        })
    );

    // Print all character names once they are fetched in order
    Promise.all(characterPromises)
      .then((names) => console.log(names.join('\n')))
      .catch((fetchErr) =>
        console.error('Error fetching character data:', fetchErr)
      );
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
}
