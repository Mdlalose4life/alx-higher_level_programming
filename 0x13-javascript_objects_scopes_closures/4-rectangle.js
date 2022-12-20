#!/usr/bin/node
class Rectangle{
    constructor(w,h){
        if (h  > 0 && w > 0){
            this.width = w;
            this.height = h;
        }
    }

        print() {
            for(let i = 1 ; i < this.height; i++){
                console.log('X', repeat(this.width))
            } 
        }
        
        rotate () {
            let temp;
            temp = this.height;
            this.height = this.width;
            this.width = temp;
        }
        
        double () {
            this.height = this.height*2;
            this.width = this.width*2;
        }
}
