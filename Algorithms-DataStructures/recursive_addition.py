# Algorithms and Data Structures: Recursion
# 03.04.2016
# @totallygloria


def Adder(num_list):

    if len(num_list) == 1:
        return num_list[0]
    else:
        return (num_list[0] + Adder(num_list[1:]))


