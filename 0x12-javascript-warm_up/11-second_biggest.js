#!/usr/bin/node
const argv = require('process').argv;

const numbers = argv.map(function (value) {
  return parseInt(value);
}).filter(function (value) {
  return !isNaN(value);
});

if (numbers.length < 2) {
  console.log(0);
} else {
  let maxIndex = numbers.indexOf(Math.max(...numbers));
  numbers.splice(maxIndex, 1);
  maxIndex = numbers.indexOf(Math.max(...numbers));
  console.log(numbers[maxIndex]);  
}
