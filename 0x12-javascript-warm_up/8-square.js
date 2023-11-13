#!/usr/bin/node

const argv = process.argv;
const side = Number.parseInt(argv[2]);
let i = 0;

if (!isNaN(side)) {
  while (i < side) {
    console.log('x'.repeat(side));
    i++;
  }
} else {
  console.log('Missing size');
}
