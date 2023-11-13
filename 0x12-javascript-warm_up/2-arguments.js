#!/usr/bin/node

const argv = process.argv;

const numofArgv = argv.length - 2;

if (numofArgv === 0) {
  console.log('No argument');
} else if (numofArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
