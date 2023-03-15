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

    //Instantiating the instance method that swap the width and height of the rectangle
    rotate(){
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
    }

    //Instantiating the instance method that doubles the size of hight and width
    double(){
        this.height = this.height*2;
        this.width = this.width*2;
    }
};