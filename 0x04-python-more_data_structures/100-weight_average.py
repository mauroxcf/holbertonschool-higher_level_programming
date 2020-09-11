#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_and_multi = (sum(map(lambda x: x[0] * x[1], my_list)))
        pond = (sum(map(lambda x: x[1], my_list)))
        return (sum_and_multi / pond)
    else:
        return 0
