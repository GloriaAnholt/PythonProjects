# Rosalinda Python Village: 5 Reading & Writing
# 11/20/15 GGuy


in_file = open("5.rosalinda.txt", "r")
output = open("5.output.txt", "r+")

i = 1

for line in in_file:
	if i % 2 == 0:
		output.write(line)
	i += 1

in_file.close()
output.close()
