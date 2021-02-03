#!/usr/bin/node

exports.addMeMaybe = function (num, recurfun) {
  /* for (let count = 0; count < num; count++) {
    return recurfun(num + 1);
  } */
  recurfun(num + 1);
};
