#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function fetchAndPrintCharacterNames(characterList, index) {
  if (index >= characterList.length) {
    console.log('Finished fetching character names.');
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.error('Error fetching character data:', error);
    } else {
      const characterData = JSON.parse(body);
      console.log('Character Name:', characterData.name);
      fetchAndPrintCharacterNames(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
  } else {
    const characterList = JSON.parse(body).characters;

    if (!characterList || characterList.length === 0) {
      console.log('No characters found for this movie.');
    } else {
      fetchAndPrintCharacterNames(characterList, 0);
    }
  }
});
