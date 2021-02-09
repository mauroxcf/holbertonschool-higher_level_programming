#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];

fs.readFile(file1, 'utf-8', function (err, data) {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data);
  }
});
