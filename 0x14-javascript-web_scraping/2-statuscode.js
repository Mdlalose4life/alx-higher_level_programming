#!usr/bin/node

const request = require('request');
const url = argv[2];


request(url, (error, response) => {
	if (error){
		console.log(error);
	}else
	console.log(response.statusCode);
});