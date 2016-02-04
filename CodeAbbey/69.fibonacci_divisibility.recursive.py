# 69: Fibonacci Divisibility
# 11/20/16  GGuy

myfile = open("69.fibonacci_data.txt", "r")
values = myfile.readlines()
fib_seq = [0, 1, 1, 2, 3]
answers = []

for i in range(len(values)):
	values[i] = values[i].strip()


def fib_calc(n):
	global fib_seq
	if len(fib_seq) <= n:
		fib_seq.append(fib_calc(n-1) + fib_calc(n-2))
	return fib_seq[n]


for num in values:
	i = 2
	while fib_calc(i) % int(num) != 0:
		i += 1
	answers.append(i)

print answers


