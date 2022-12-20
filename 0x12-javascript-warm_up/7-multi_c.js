#!/usr/bin/node
let index;
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (index = 0; index < num; index++) {
    console.log('C is fun');
  }
}
