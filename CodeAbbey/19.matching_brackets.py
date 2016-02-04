# 19: Matching Brackets
# 11/16/2015 GGuy



myfile = open("bracket_data.txt", "r")
bracket_results = open("bracket_results.txt", "w")

my_stack = []

for line in myfile:
	for char in line:
		if char == "(" or char == "[" or char == "{" or char == "<":
			my_stack.append(char) 
		elif char == ")" or char == "]" or char == "}" or char == ">":		
			if len(my_stack) > 0:
				temp = my_stack.pop()
			else:
				bracket_results.write("0 \n")
				break
			
			if temp == "(" and char != ")":
				bracket_results.write("0 \n")
				break
			elif temp == "[" and char != "]":
				bracket_results.write("0 \n")
				break
			elif temp == "{" and char != "}":
				bracket_results.write("0 \n")
				break
			elif temp == "<" and char != ">":
				bracket_results.write("0 \n")
				break
	
			elif char == "\n" and len(my_stack) > 0:
				bracket_results.write("0 \n")
				break		
		
	else:
		bracket_results.write("1 \n")
