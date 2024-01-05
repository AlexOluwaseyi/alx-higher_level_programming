#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const todos = JSON.parse(body);
  const tasksCompleted = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId]++;
      } else {
        tasksCompleted[todo.userId] = 1;
      }
    }
  }
  console.log(tasksCompleted);
});
