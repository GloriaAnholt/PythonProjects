# CodeAbbey: #5 Min of Three
# 12.30.2015
# @totallygloria

in_file = open('05.min_of_three.data.txt')

list_of_mins = []

for line in in_file.readlines():
	a, b, c = line.split(' ')
	a, b, c = int(a), int(b), int(c)
	d = min(a,b,c)
	list_of_mins.append(d)

for num in list_of_mins:
	print num,
