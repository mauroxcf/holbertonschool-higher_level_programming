#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const newDict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    for (let i = 0; i < info.length; i++) {
      if (info[i].completed === true) { // filter only the completed task
        if (newDict[info[i].userId] === undefined) { // create the first key
          newDict[info[i].userId] = 1;
        } else {
          newDict[info[i].userId]++; // increase the value each time
        }
      }
    }
    console.log(newDict);
  }
});
