#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if idx > len(my_list):
            return(my_list)
        else:
            del my_list[idx]
        return(my_list)
