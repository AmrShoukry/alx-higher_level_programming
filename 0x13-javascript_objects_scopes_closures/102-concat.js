#!/usr/bin/node
const fs = require('fs');
const argv = require('process').argv;

const file1Content = fs.readFileSync(argv[2], 'utf-8');
const file2Content = fs.readFileSync(argv[3], 'utf-8');

fs.writeFileSync(argv[4], file1Content + file2Content, 'utf-8');
