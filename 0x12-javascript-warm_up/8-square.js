#!/usr/bin/node

const argv = process.argv;
const side = Number.parseInt(argv[2]);
let i = 0;

if (!isNaN(side) && side > 0) {
  while (i < side) {
    console.log('X'.repeat(side));
    i++;
  }
} else if (isNaN(side)) {
  console.log('Missing size');
}
