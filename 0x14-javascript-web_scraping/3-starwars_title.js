#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id';
const movie_Id = process.argv[2];

request(url + movie_Id, function(error, response, body){
	if(error) {
		console.log(error);
	}
	else{
		console.log(JSON.parse(body).title);
	}
});
