#!/usr/bin/node

if (parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  let height;

  for (height = 0; height < size; height++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
