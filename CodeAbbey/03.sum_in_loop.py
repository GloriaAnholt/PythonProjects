# CodeAbbey: #3 Sum in Loop
# 12.30.2015
# @totallygloria

in_file = open('03.sum_in_loop.data.txt')

list_of_sums = []

for line in in_file.readlines():
	a, b = line.split(' ')
	list_of_sums.append(int(a)+int(b))
	

for item in list_of_sums:
	print item,
