#!/usr/bin/node

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + String(movieId);

const request = require('request');
request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  for (const character of movie.characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }
      const characterObject = JSON.parse(body);
      console.log(characterObject.name);
    });
  }
});
