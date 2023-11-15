#!/usr/bin/node

exports.esrever = function (list) {
  const n = list.length;
  for (let i = 0; i < n; i++) {
    for (let j = n - 1; j >= 0; j--) {
      let newList[i] = list[j];
    }
  }
  return newList;
};
