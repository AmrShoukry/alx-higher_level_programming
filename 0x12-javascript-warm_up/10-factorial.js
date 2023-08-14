#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 0 || number === 1) {
    return (1);
  }
  return (number * factorial(number - 1));
}

const argv = require('process').argv;
const number = parseInt(argv[2]);
console.log(factorial(number));
