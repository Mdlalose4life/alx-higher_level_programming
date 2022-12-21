#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
    charPrint(c){
        if (c === undefinded){
             c = 'X';
        }else{
            for(i = 0; i < this.height; i++)
            console.log(c.repeat(this.width)); 
        }   
    }
};
