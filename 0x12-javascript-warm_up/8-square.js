#!/usr/bin/node
const args = parseInt(process.argv[2], 10);
const myVar = 'X';

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < args; index++) {
    console.log(myVar.repeat(args));
  }
}
