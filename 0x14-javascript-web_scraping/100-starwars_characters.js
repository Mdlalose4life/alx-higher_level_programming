#!/usr/bin/node

const request = require('request')

const movie_id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/films/${movie_id}/`

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const character = data.characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error){
          console.log(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name)
    });
  }
});