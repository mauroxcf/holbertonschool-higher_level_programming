#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let argument = process.argv.splice(2); // remove first 2 argument
  argument = argument.map(x => parseInt(x)); // mapping the array
  const maxValue = Math.max(...argument); // obtain max value using spread op.
  argument.splice(argument.indexOf(maxValue), 1); // remove max value
  const secMax = Math.max(...argument); // obtain again max value

  console.log(parseInt(secMax));
}
