# CodeAbbey: #6 Rounding
# 12.30.2015
# @totallygloria

in_file = open('06.rounding.data.txt')

list_of_rounds = []

for line in in_file.readlines():
	a, b, = line.split(' ')
	a, b = float(a), float(b)
	c = a / b
	if c >= 0 and (c + 0.5) >= (int(c) + 1):
		list_of_rounds.append(int(c)+1)
	elif c < 0 and (c - 0.5) <= (int(c) - 1):
		list_of_rounds.append(int(c)-1)
	else:
		list_of_rounds.append(int(c))

for num in list_of_rounds:
	print num,
