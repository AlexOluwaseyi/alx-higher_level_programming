#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const baseUrl = process.argv[2];
const file = process.argv[3];

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  fs.writeFile(file, body, { encoding: 'utf-8', flag: 'w' }, (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
