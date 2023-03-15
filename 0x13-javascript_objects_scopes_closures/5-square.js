#!/usr/bin/node

const Rectangle = require("./0-rectangle");

/*A Class Square that inherits from Class Rectangle*/

module.exports = class Square extends Rectangle{
    constructor(size){
        super(size,size);
    }

};