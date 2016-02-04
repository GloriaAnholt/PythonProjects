# CodeAbbey: Problem 12 - Modulo and Time Difference
# 01/05/2016
# @totallygloria

"""
Essentially everything about this is gross and shameful.
All of it should be scrapped, instead:
    Use a generator instead of a loop for the data grabbing
    Create some data structure or something for conversions (dict?)
    Separate into/out of seconds into two function calls?
    Actually use TDD to make this less gross.
"""

infile = open('time_difference.data.txt')


def sec_calc(data):
    for line in data.readlines():
        day1, hour1, min1, sec1, day2, hour2, min2, sec2 = line.split()

        starting_seconds = (int(day1) * 24 * 60 * 60) + \
                           (int(hour1) * 60 * 60) + (int(min1) * 60) + (int(sec1))
        ending_seconds = (int(day2) * 24 * 60 * 60) + (int(hour2) * 60 * 60) + \
                         (int(min2) * 60) + (int(sec2))
        total_seconds = ending_seconds - starting_seconds
        end_sec = total_seconds % 60
        end_min = ((total_seconds - end_sec) / 60) % 60
        end_hour = ((((total_seconds - end_sec) / 60) - end_min) / 60) % 24
        end_day = (((((total_seconds - end_sec) / 60) - end_min) / 60) - end_hour) / 24

        print '(%d %d %d %d)' % (end_day, end_hour, end_min, end_sec),


sec_calc(infile)
