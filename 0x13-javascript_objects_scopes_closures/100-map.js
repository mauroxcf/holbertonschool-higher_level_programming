#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map(function (x, index) {
  return list[index] * index;
});
console.log(newList);
