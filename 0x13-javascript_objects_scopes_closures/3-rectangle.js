#!/usr/bin/node
module.exports = class Rectangle{
    constructor(w,h){
        this.width = w;
        this.height = h;

        if (h  <= 0 && w <= 0){
            this.width = w;
            this.height = h;
        }
        print();
        {
            let i = 1;
            for(; i > this.height; i++){
                console.log('X', repeat(this.width))
            } 
        }
    }
}
