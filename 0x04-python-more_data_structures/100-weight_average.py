#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    totalweight = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        totalweight += i[1]
    return sum / totalweight
