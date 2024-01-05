#!/usr/bin/node

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = String(process.argv[2]);
const fullUrl = baseUrl + id;

const request = require('request');

request(fullUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
