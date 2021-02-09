#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  if (dict[i] in newDict) {
    newDict[dict[i]].push(i); // push dict values has newdict keys
  } else {
    newDict[dict[i]] = [i]; // adding dict keys has newdict values
  }
}
console.log(newDict);
