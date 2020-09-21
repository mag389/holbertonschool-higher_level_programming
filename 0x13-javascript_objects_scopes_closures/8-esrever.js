#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];
  for (let i = list.length; i > 0; i--) {
    rlist.push(list[i - 1]);
  }
  return rlist;
};
