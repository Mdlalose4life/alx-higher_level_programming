#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        new_string = (my_string.translate({ord(i): None for i in 'c'}))
        new_string = (new_string.translate({ord(i): None for i in 'C'}))
            return new_string
