#!/usr/bin/node
let lognum = 0;
exports.logMe = function (item) {
  console.log(lognum + ': ' + item);
  lognum++;
};
