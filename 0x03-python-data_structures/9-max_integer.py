#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        big_num = num1 = num2 = my_list[i]
        if len(my_list) == 0:
            return None
        if num1 > num2:
            num1 = big_num
        elif num2 > num1:
            num2 = big_num
            return big_num
