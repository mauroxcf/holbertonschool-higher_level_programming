#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_0 = (0, 0)
    tuple_sum1 = tuple_a + tuple_0
    tuple_sum2 = tuple_b + tuple_0
    return (tuple_sum1[0] + tuple_sum2[0], tuple_sum1[1] + tuple_sum2[1])
