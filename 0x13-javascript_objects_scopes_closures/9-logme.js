#!/usr/bin/node
let i = 0;
exports.logme = function (item) {
    console.log('${i++}: ${item}')
};
