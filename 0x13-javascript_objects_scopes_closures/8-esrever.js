#!/usr/bin/node
exports.esrever = function (list){
    let revString = "";
    for (let i = list.length - 1; i >= 0; i--){
        revString += list[i];
    }
    return revString;
}