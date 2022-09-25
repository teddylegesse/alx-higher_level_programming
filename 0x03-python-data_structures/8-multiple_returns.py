#!/usr/bin/python3
def multiple_returns(sentence):
    len_char = len(sentence)

    if (len_char == 0):
        result = (len_char, None)
    else:
        result = (len_char, sentence[0])

    return (result)
