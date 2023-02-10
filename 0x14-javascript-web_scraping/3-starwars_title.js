#!/usr/bin/env node

const request = require('request')
response = request.get('https://swapi-api.alx-tools.com/api/films/:id')
console.log(response)