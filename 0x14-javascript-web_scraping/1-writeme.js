#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const wText = process.argv[3];

fs.writeFile(file1, wText, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
