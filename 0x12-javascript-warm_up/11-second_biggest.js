#!/usr/bin/node

if (process.argv.length <= 3 ) {
  console.log(0);
} else {
  const arguments = process.argv.slice(2); // remove first 2 arguments
  let maxValue = Math.max.apply(null, arguments); // obtain max value
  arguments.slice(arguments.indexOf(maxValue), 1); // remove max value
  let secMax = Math.max.apply(null, arguments); // obtain again max value

  console.log(parseInt(secMax));
}
