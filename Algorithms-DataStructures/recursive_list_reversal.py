# Algorithms & Data Structures: Recursive Exercises
# 03.29.16
# @totallygloria


'''
Write a recursive function to reverse a list.
'''


def rev_list(sample):
	
	new_list = []
	
	if len(sample) == 1:
		new_list.append(sample[0])
	else:
		new_list.append(sample[-1])
		sample.pop()
		new_list.append(rev_list(sample))
		
	return new_list
	

print rev_list([1,2,3,4,5])

		
