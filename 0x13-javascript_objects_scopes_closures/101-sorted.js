#!/usr/bin/node

const dict = require('./101-data').dict;

// Create a new dictionary to store the number of occurrences by user id
const userIdsByOccurrence = {};

// Iterate through the dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the number of occurrences is not in the new dictionary, add it
  if (userIdsByOccurrence[occurrence] === undefined) {
    userIdsByOccurrence[occurrence] = [];
  }

  // Add the user id to the list of user ids for this occurrence
  userIdsByOccurrence[occurrence].push(userId);
}
console.log(userIdsByOccurrence);
