#!/usr/bin/node
const argv = require('process').argv;
const number = parseInt(argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    const array = [];
    for (let j = 0; j < number; j++) {
      array.push('X');
    }
    console.log(array.join(''));
  }
}
