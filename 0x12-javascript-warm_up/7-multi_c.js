#!/usr/bin/node

const argv = process.argv;
const argvConv = Number.parseInt(argv[2]);
let count = 0;

if (!isNaN(argvConv)) {
  while (count < argvConv) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
