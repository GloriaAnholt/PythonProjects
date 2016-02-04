# CodeAbbey: Problem 11 - Sum of digits in a calculated number
# 01/05/2016
# @totallygloria

infile = open('11.sum_of_digits.data.txt')
number_list = []

for line in infile.readlines():
    number_list.append(line.split())


def initial_math(num_list):
    # multiply the first two, add the third
    digits_list = []

    for line in num_list:
        a = line[0]
        b = line[1]
        c = line[2]
        total = int(a)*int(b)+int(c)
        digits_list.append(int(total))

    return digits_list

def digit_add(dig_list):
    # add the digits
    summed_digits = []

    for num in dig_list:
        total = 0
        while num > 0:
            total += (num % 10)
            num /= 10
        summed_digits.append(total)

    return summed_digits

print digit_add(initial_math(number_list))