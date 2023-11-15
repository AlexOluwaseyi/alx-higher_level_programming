#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

if (typeof argv[2] !== 'undefined' && typeof argv[3] !== 'undefined' && typeof argv[4] !== 'undefined') {
  fs.readFile(argv[2], 'utf-8', (err, file1) => {
    if (err) throw err;
    fs.readFile(argv[3], 'utf-8', (err, file2) => {
      if (err) throw err;
      const concText = file1 + file2;

      fs.writeFile(argv[4], concText, (err) => {
        if (err) throw err;
      });
    });
  });
}
