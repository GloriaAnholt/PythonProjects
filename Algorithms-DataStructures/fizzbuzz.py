# Programming Problems: Implement a Fizz Buzz Counter
# 12.29.2015
# @totallygloria


# check if mod 3 or 5 or 15 and replace
# append to list

def fizzbuzz_generator(desired_len):
    fb_list = []

    for num in range(1, desired_len+1):
        if num % 15 == 0:
            fb_list.append('FizzBuzz')
        elif num % 3 == 0:
            fb_list.append('Fizz')
        elif num % 5 == 0:
            fb_list.append('Buzz')
        else:
            fb_list.append(num)

    return fb_list
