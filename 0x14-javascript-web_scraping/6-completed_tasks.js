#!/usr/bin/node

const request = require('request');
const obj = {};

request(process.argv[2], function (error, response, body) {
  if (error);
  const RESULTS = JSON.parse(body);

  RESULTS.forEach(user => {
    if (!(user.userId in obj) && user.completed === true) {
      obj[user.userId] = 1;
    } else if (user.completed === true) {
      obj[user.userId]++;
    }
  });

  console.log(obj);
});
