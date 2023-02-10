#!/usr/bin/node

const request = require(request)
const movie_Id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/ + movie_Id';

request(url, function(error, response, body){
	if(error) {
		console.log(error);
	}
	else{
		console.log(JSON.parse(body).title);
	}
});
