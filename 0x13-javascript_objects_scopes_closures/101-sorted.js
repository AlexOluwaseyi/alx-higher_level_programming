#!/usr/bin/node

const data = require('./101-data');

const occurrencesByUserId = data.dict;

const usersByOccurrences = {};

for (const userId in occurrencesByUserId) {
  const occurrences = occurrencesByUserId[userId];

  if (!usersByOccurrences[occurrences]) {
    usersByOccurrences[occurrences] = [];
  }

  usersByOccurrences[occurrences].push(userId);
}

console.log(usersByOccurrences);
