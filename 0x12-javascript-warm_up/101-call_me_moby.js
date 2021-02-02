#!/usr/bin/node

exports.callMeMoby = function (num, theFunction) {
  for (let count = 0; count < num; count++) {
    theFunction();
  }
};
