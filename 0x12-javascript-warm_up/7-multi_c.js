#!/usr/bin/node

if (parseInt(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  let count;
  for (count = 0; count < num; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
