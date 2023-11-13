#!/usr/bin/node

const argv = process.argv[2];
const argvConv = Number.parseInt(argv);

function factorial(n) {
  if (n >= 1) {
    let result = n * factorial(n - 1);
    return result;
  } else {
    return 1;
  }
}

if (!isNaN(argvConv)) {
  solution = factorial(argvConv);
  console.log(solution);
} else {
  console.log(1);
}
