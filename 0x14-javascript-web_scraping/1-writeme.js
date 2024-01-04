#!/usr/bin/node

const file = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(file, string, { encoding: 'utf-8', flag: 'w' }, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
