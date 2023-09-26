#!/usr/bin/node

const request = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(URL, function (error, response, body) {
  if (error);
  console.log(JSON.parse(body).title);
});
