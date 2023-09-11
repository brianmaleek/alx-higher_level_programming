#!/usr/bin/node

// Convert command-line arguments to integers
const args = process.argv.slice(2).map(arg => parseInt(arg));

// Remove NaN values and sort the integers in ascending order
const sortedArgs = args.filter(arg => !isNaN(arg)).sort((a, b) => a - b);

// Check if there are at least two valid integers
if (sortedArgs.length >= 2) {
  // Print the second-to-last element (the second biggest integer)
  console.log(sortedArgs[sortedArgs.length - 2]);
} else {
  // Print 0 if no arguments passed or only one argument is provided
  console.log(0);
}
