#!/usr/bin/node

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + String(movieId);

const sortedCharacters = [];
const request = require('request');

const getCharacterData = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

request(baseUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  for (const character of movie.characters) {
    try {
      const characterName = await getCharacterData(character);
      sortedCharacters.push(characterName);
    } catch (error) {
      console.error(error);
      process.exit(1);
    }
  }

  sortedCharacters.forEach(item => {
    console.log(item);
  });
});
