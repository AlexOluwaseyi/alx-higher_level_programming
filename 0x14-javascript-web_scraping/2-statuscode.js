#!/usr/bin/node

const url = process.argv[2];

const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
