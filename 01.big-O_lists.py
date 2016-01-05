# Algorithms & Data Structures: Algorithm Analysis
# 12.21.15
# @totallygloria


items = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def compare_once():
	
	items = [21,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	min_num = items[0]
	
	for i in items:
		if i < min_num:
			min_num = i
	
	return min_num


def compare_all(items):
	
	pass
	# the example picked a number, compared it to everything, then picked
	# the next number and compared it to everything. This is obviously 
	# dumb, and was actually a lot less clear than the other example
	# which matched mine.



if __name__ == '__main__':
	import timeit
	for i in range(11):
		print timeit.timeit("compare_all()", setup="from __main__ import compare_all", number=1000)
