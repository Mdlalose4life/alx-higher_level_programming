#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
return list.filter(occurance => occurance === searchElement).length;
};
