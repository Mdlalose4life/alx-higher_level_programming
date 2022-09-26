#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    # test the len
    if length == 0:
        return (0, None)
    else:
        return (length, sentence[0])
