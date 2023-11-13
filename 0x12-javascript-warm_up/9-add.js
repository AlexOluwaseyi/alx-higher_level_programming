#!/usr/bin/node

const argv1 = process.argv[2];
const argv2 = process.argv[3];

const argv1Conv = Number.parseInt(argv1);
const argv2Conv = Number.parseInt(argv2);

if (isNaN(argv1Conv) || isNaN(argv2Conv)) {
  console.log('NaN');
} else {
  console.log(argv1Conv + argv2Conv);
}
