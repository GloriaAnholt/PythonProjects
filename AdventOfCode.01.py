# Advent Calendar of Code: 01 
# 12.04.15
# @totallygloria

in_file = open("advent.01.data.py", "r")
parens = in_file.read()

floor = 0
position = []

for i in range(len(parens)):
	if parens[i] == "(":
		floor += 1
	elif parens[i] == ")":
		floor -= 1
		if floor == -1:
			position.append(i+1)
 

print floor, position
