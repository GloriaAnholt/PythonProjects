# CodeAbbey: Problem 11 - Sum of digits in a calculated number
# 01/05/2016
# @totallygloria

infile = open('11.sum_of_digits.data.txt')
number_list = []

for line in infile.readlines():
    number_list.append([line.split()])


def initial_math(num_list):
''' multiply the first two, add the third '''
    digits_list = []

    for line in num_list:
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        digits_list.append(a*b+c)

    return digits_list


# add the digits