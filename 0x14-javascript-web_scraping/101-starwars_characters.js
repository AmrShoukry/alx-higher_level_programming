#!/usr/bin/node

const request = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/`;

request(URL, function (error, response, body) {
  if (error);
  const CHARACTERS = JSON.parse(body).results[process.argv[2] - 1].characters;
  CHARACTERS.forEach(characterURL => {
    request(characterURL, function (error2, response2, body2) {
      console.log(JSON.parse(body2).name);
    });
  });
});
