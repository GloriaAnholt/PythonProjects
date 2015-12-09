# Advent Calendar of Code: 05
# 12.08.15
# @totallygloria

'''
a pair of any two letters that appears at least twice
one letter which repeats with exactly one letter between them, like xyx
'''

import re

in_file = open("advent.05.data.py", "r")


def line_checker(data):
	
	nice = 0
	double = re.compile(r'(?P<double>([a-z]){2}).*(?P=double)')
	xyx = re.compile(r'(?P<letter>[a-z])\w(?P=letter)')
	
	for line in data:
		if re.search(double, line) == None:
			pass
		elif re.search(xyx, line) == None:
			pass
		else:
			print "nice", line
			nice += 1
	
	print nice
			
			

line_checker(in_file)


