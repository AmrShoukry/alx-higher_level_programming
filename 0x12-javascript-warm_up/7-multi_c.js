#!/usr/bin/node
const argv = require('process').argv;
const numberOfOccurences = parseInt(argv[2]);
if (isNaN(numberOfOccurences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOccurences; i++) {
    console.log('C is fun');
  }
}
