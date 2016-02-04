# CodeAbbey: #4 Min of Two
# 12.30.2015
# @totallygloria

in_file = open('04.min_of_two.data.py')

list_of_mins = []

for line in in_file.readlines():
	a, b = line.split(' ')
	a, b = int(a), int(b)
	c = min(a,b)
	list_of_mins.append(c)

for num in list_of_mins:
	print num,
