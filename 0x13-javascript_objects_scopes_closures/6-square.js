#!/usr/bin/node

const Squares = require('./5-square.js');
module.exports = class Square extends Squares {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        process.stdout.write(c.repeat(this.width));
        console.log();
      }
    } else {
      this.print();
    }
  }
};
