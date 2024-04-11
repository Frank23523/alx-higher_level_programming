#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (let len = list.length - 1; len >= 0; len--) {
    revList.push(list[len]);
  }
  return revList;
};
