# Advent Calendar of Code: 04
# 12.06.15
# @totallygloria


import hashlib
import itertools


def brute_force(given):
	
	for i in itertools.count(0):
		cur_num = str(i)
		a = hashlib.md5()
		a.update(given+cur_num)
		cur_hex = a.hexdigest()

		if cur_hex[0:6:1] == "000000":
			print "current hex checks out:", cur_hex
			print "i equals", i
			return cur_hex


brute_force("bgvyzdsv")

'''
given1 = "abcdef"
test1 = brute_force(given1)

given2 = "pqrstuv"
test2 = brute_force(given2)


if test1[0:11:1] == "000001dbbfa":
	print "test1 works"
else:
	print "doesn't match test1 results"
	
if test2[0:11:1] == "000006136ef":
	print "test2 works"
else:
	print "doesn't match test2 results"
'''
