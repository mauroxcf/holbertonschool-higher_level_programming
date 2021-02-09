#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file1 = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = body;
    fs.writeFile(file1, info, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
