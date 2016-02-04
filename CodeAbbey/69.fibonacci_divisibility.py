# 69: Fibonacci Divisibility
# 11/20/16  GGuy

myfile = open("69.fibonacci_data.txt", "r")
values = myfile.readlines()
fib_seq = [0, 1, 1, 2, 3]
answers = []

for i in range(len(values)):
    values[i] = values[i].strip()

largest = sorted(values)[-1]


i = 4
while fib_seq[i] % int(largest) != 0:
    fib_seq.append(fib_seq[i-1] + fib_seq[i])
    i += 1

for num in values:
    for i in range(1, len(fib_seq)):
        if fib_seq[i] % int(num) == 0:
            answers.append(i)
            break

print answers
