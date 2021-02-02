#!/usr/bin/node

const factNumber = parseInt(process.argv[2]);

console.log(factorial(factNumber));
function factorial (num) {
  if (!num || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1); // using to calculate factorial
  }
}
