#!/usr/bin/node

const argv = process.argv[2];
const argvConv = Number.parseInt(argv);

if (!isNaN(argvConv)) {
  console.log('My number: ' + argvConv);
} else {
  console.log('Not a number');
}
