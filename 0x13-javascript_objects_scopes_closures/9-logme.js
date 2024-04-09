#!/usr/bin/node
let numofarg = 0;

exports.logMe = function (item) {
  console.log(numofarg + ': ' + item);
  numofarg++;
};
