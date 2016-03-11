# Cracking the Coding Interview
# p 79 - converting between hex and binary
# 3/11/2016
# @totallygloria



def convert_10(num, base):
	
	lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	int_sum = 0

	for i in range(len(num)):  # counts bases from zero up, walks backward through string
		int_sum += (base ** i) * lookup.index(num[-1 - i])
	
	return int_sum


def compare_nums(num1, base1, num2, base2):
	
	if (base1 < 2 or base1 > 35) or (base2 < 2 or base2 > 35):
		return None
	
	return (convert_10(num1, base1)) == (convert_10(num2, base2))
			

print compare_nums("110", 1, "0", 16) 
print compare_nums("110", 2, "0", 59) 

print compare_nums("0", 2, "0", 16)
print compare_nums("5", 10, "5", 10)
print compare_nums("111", 2, "7", 16)
print compare_nums("167", 10, "A7", 16)
print compare_nums("11100111", 2, "E7", 16)

print compare_nums("110111", 2, "B4", 16)
print compare_nums("1110011", 4, "E", 16)
print compare_nums("110111", 2, "E7", 12)





"""
Problems in the first run:
  * Tried to do a dict-like look-up, instead of using .index
  * Used a stack and then needed a second loop to unpack it
  * forgot to convert the values with str()
  * almost forgot to add the last value (the second add outside of the loop)
  * had to solve the binary part by hand by counting it out to figure out order
  * some basic syntax errors (all caught immediately, but need to be more careful)
  * Doesn't work, you need to use a stack!
  
Problems with second try:
  * didn't check if the base < 2 or greater than the lookup index
  * tried to name the variable sum, which is a reserved word
  * counted UP the digits, instead of down
  * Added a return None inside the comparison funct to return None instead
    of calling the convert function if the bases are out of range
"""
