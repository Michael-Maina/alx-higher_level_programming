#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tasksDict = {};
    const todos = JSON.parse(body);
    for (const task of todos) {
      const key = task.userId;
      if (task.completed === true) {
        if (tasksDict[key] === undefined) {
          tasksDict[key] = 1;
        } else {
          tasksDict[key]++;
        }
      }
    }
    console.log(tasksDict);
  }
});
