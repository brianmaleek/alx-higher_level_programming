#!/usr/bin/python3
def weight_average(my_list=[]):

    if my_list == []:
        return (0)

    score_total = 0
    weight_div = 0
    for i in my_list:
        score_total += i[0] * i[1]
        weight_div += i[1]
    return (score_total / weight_div)
