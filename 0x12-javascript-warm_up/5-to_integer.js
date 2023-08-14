#!/usr/bin/node
const argv = require('process').argv;
const number = parseInt(argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
