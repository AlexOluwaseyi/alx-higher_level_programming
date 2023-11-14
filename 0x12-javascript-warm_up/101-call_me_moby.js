#!/usr/bin/node

exports.callMeMoby = function (x, thefunction) {
  let n = 0;
  while (n < x) {
    thefunction();
    n++;
  }
};
