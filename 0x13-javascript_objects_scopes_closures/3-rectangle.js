#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }

    // Instantiate the instance method print that prints the X of rectangles
    print() {
        for (let i = 0; i < this.height; i++){
            console.log('X'.repeat(this.width));
        }
    }
};