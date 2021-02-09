#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const wText = process.argv[3];

fs.writeFile(file1, wText, err => {
  if (err) {
    console.log(err);
  } else {
    console.log(fs.readFileSync(file1, 'utf8'));
  }
});
