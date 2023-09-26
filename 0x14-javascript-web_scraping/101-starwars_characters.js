#!/usr/bin/node

const request = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(URL, function (error, response, body) {
  if (error);
  const CHARACTERS = JSON.parse(body).characters;
  CHARACTERS.forEach(characterURL => {
    request(characterURL, function (error2, response2, body2) {
      console.log(JSON.parse(body2).name);
    });
  });
});
