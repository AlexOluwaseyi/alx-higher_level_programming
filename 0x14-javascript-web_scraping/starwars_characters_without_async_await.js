#!/usr/bin/node

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + String(movieId);

const sortedCharacters = [];
const request = require('request');

const getCharacterData = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
		  process.exit(1);
	  }
      resolve(JSON.parse(body).name);
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
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }
//      const characterObject = JSON.parse(body);
//      const characterName = characterObject.name;
//      sortedCharacters.push(characterName);
//      console.log(sortedCharacters);
//      console.log(characterObject.name);
	  const characterName = await getCharacterData(character);
	  sortedCharacters.push(characterName);
    });
	  console.log(sortedCharacters);
  }
  console.log(sortedCharacters);
  sortedCharacters.forEach(item => {
    console.log(item);
  });
});
