#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple_result = (len(sentence), sentence[0])
        return tuple_result
    else:
        return (0, None)
