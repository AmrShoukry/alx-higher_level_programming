#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv[2], function (error, response, body) {
  if (error);
  JSON.parse(body).results.forEach(film => {
    film.characters.forEach(url => {
      if (url === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    });
  });
  console.log(count);
});
