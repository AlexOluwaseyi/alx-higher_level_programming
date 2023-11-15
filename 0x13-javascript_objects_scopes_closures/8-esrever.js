#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const n = list.length;
  for (let i = n - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
