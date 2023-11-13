#!/usr/bin/node

const argv = process.argv[2];

if (typeof argv === 'undefined') {
  console.log('No argument');
} else {
  console.log(argv);
}
