#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first_charactor = sentence[0]
     else:
        first_charactor = None
    return (length, first_charactor)
