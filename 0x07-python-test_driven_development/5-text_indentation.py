#!/usr/bin/python3
"""
This is module 5-text_indentation.py
This module that prints text after a new two lines after ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    ind = 0
    for i in text:
        if ind == 0:
            if i == ' ':
                continue
            else:
                ind = 1
        if ind == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                ind = 0
            else:
                print(i, end='')
