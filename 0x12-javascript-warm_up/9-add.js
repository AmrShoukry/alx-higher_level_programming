#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const argv = require('process').argv;
const number1 = parseInt(argv[2]);
const number2 = parseInt(argv[3]);
add(number1, number2);
