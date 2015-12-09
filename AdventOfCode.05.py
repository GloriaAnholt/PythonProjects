# Advent Calendar of Code: 05
# 12.08.15
# @totallygloria

'''
can't contain: ab, cd, pq, or xy
must contain one doubled letter
must contain: 3 vowels
'''

import re

in_file = open("advent.05.data.py", "r")


def line_checker(data):
	
	nice = 0
	double = re.compile(r'((\w)\2)+')
	vowels = re.compile('([aeiou]).*([aeiou]).*([aeiou])')
	
	for line in data:
		if ("ab" in line) or ("cd" in line) or ("pq" in line) or ("xy" in line):
			pass
		elif re.search(double, line) == None:
			pass
		elif re.search(vowels, line) == None:
			pass
		else:
			nice += 1
	print nice
			
			
line_checker(in_file)

