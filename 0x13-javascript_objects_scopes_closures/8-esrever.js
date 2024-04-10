#!/usr/bin/node

exports.esrever = function (list) {
  let rev_list = []
  for (let len = list.length - 1; len >=0; len--) {
    rev_list.push(list[len]);
  }
  return rev_list;
};
