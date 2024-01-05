#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const full = JSON.parse(body);
  let count = 0;

  for (const movies of full.results) {
    for (const character of movies.characters) {
      if (character.includes('/people/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
