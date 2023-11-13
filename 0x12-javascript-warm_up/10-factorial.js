#!/usr/bin/node

const argv = process.argv[2];
const argvConv = Number.parseInt(argv);

function factorial (n) {
  if (n >= 1) {
    const result = n * factorial(n - 1);
    return result;
  } else {
    return 1;
  }
}

if (!isNaN(argvConv)) {
  const solution = factorial(argvConv);
  console.log(solution);
} else {
  console.log(1);
}
