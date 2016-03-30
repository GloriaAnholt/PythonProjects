# Algorithms & Data Structures: Recursive Exercises
# 03.29.16
# @totallygloria


'''
Write a recursive function to compute the factorial of a number
'''


def factorial_calc(num):
	
	if num <= 1:
		return 1
	else:
		total = num * factorial_calc(num-1)
	
	return total 
	



		
