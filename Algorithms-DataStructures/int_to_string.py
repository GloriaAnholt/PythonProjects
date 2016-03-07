# Algorithms and Data Structures: Recursion
# 03.07.2016
# @totallygloria



def int_to_string(num, base):
    """
    1. Reduce the original number to a series of single-digit numbers.
    2. Convert the single digit-number to a string using a lookup.
    3. Concatenate the single-digit strings together to form the final result.
    """

    convert_string = "0123456789ABCDEF"

    if base < 2 or base > 16:
        print "Base must be between 2 and 16"
        return
    
    if num < base:
        return convert_string[num]
    else:
        return int_to_string(num/base, base) + convert_string[num % base]


int_to_string(1234,17)


def reverse_a_string(string):
    # Write a function that takes a string as a parameter and returns a new string
    # that is the reverse of the old string.

    if len(string) == 0:
        return string
    elif len(string) <= 1:
        return string[0]
    else:
        return reverse_a_string(string[1:]) + string[0]


print 'this is the test string'
print reverse_a_string('this is the test string')
print (reverse_a_string('this is the test string') == 'this is the test string'[::-1])
