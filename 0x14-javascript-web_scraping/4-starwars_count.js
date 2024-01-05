#!/usr/bin/node

const request = require('request');

const baseUrl = process.argv[2];
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const full = JSON.parse(body);
  let count = 0;

  const wedgeId = String(18);
  for (const movies of full.results) {
    if (movies.characters.includes(peopleUrl + wedgeId + '/')) {
      count++;
    }
  }
  console.log(count);
});
