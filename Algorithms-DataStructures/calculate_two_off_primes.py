# Algorithms / Hash Table: Calculating Two-Off Primes
# 4.26.2016
# @totallygloria

"""
Takes a list of the first 10,000 primes and populates a list with any that are
exactly two larger than a neighboring prime.
"""


def massage_primes():

    raw_data = open('primes.txt', 'r')
    primes = []
    two_off_primes = []

    for line in raw_data:
        primes.extend([int(n) for n in line.strip().split()])

    for i in range(1,10000):
        if (primes[i-1] + 2) == primes[i]:
            two_off_primes.append(primes[i])

    print two_off_primes

massage_primes()


