#!/usr/bin/node

const argv = process.argv;
let first = 0;
let second = 0;
let temp = 0;
let n = 2;

if (typeof argv[2] !== 'undefined') {
  while (n < argv.length) {
    if (first === 0) {
      first = Number.parseInt(argv[n]);
    } else if (first !== 0 && second === 0) {
      temp = first;
      if (first > Number.parseInt(argv[n])) {
        second = Number.parseInt(argv[n]);
        temp = 0;
      } else if (first < Number.parseInt(argv[n])) {
        first = Number.parseInt(argv[n]);
        second = temp;
        temp = 0;
      }
    } else if (first !== 0 && second !== 0) {
      if (first > Number.parseInt(argv[n])) {
        if (second < Number.parseInt(argv[n])) {
          second = Number.parseInt(argv[n]);
        }
      } else {
        temp = first;
        first = Number.parseInt(argv[n]);
        second = temp;
        temp = 0;
      }
    }
    n++;
  }
}
console.log(second);
