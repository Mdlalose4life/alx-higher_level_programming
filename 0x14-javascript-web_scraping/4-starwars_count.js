#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterID = '18';
let count = 0;

request(url, (error, response, body) =>{
  if(error){
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.character.forEach((characterID) => {
        if(character.includes(characterID)){
        count += 1

                }
            });
        });
        console.log(count);
    }
});