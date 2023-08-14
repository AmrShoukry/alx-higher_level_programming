#!/usr/bin/node
const argv = require('process').argv;

let counter = 0;

for (let i = 2; i < argv.length; i++) {
  counter++;
}

if (counter === 0) {
  console.log('No argument');
} else if (counter === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
