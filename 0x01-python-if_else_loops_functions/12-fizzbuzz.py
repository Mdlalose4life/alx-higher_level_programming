#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
    if c % 3 == 0 and c % 5 == 0:
        print('fizzbuzz', end=' ')
    elif c % 3 == 0:
        print('Fizz', end=' ')
    elif c % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(c, end=' ')
