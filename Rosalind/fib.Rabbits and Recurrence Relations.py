# Fib: Rabbits and Recurrence Relations
# 11/24/15

'''
n1 = 1
n2 = 1
n3 = (n1 * k) + n2
n4 = (n2 * k) + n3
n5 = (n3 * k) + n4
'''
fib_seq = [1, 1]

def fucking_rabbits(n):
	global fib_seq
	k = 2
	if len(fib_seq) <= n:
		fib_seq.append((fucking_rabbits(n-2) * k) + fucking_rabbits(n-1))
	return fib_seq[n]

print fucking_rabbits(33)
