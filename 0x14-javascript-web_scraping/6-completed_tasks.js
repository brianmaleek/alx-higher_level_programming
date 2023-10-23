#!/usr/bin/node

/**
 * Script computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 * You must use the module request
 */

const request = require('request');

// Check if URL is provided
if (process.argv.length < 3) {
  console.log('Usage: node 6-completed_tasks.js <URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make GET request to the API endpoint
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Invalid URL');
  } else {
    const data = JSON.parse(body);
    const completedTasks = {};
    data.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId] += 1;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
