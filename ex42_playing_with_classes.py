# Exercise 42: Is-A, Has-A --> Practice with classes and objects
# 10/19/2015


class Person():
	
    def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
	
Phonebook = set([])

def user_input():
	print "What is your name?"
	input_name = raw_input('> ')

	print "What is your age?"
	input_age = raw_input('> ')

	print "What is your gender?"
	input_gender = raw_input('> ')

	test_person = Person(input_name, input_age, input_gender)
	
	Phonebook.add((test_person.name, test_person.age, test_person.gender))


print "Do you want to enter a person?"
repeat = raw_input('> ').lower()

while (repeat == 'y' or repeat == 'yes'):
	user_input()
	print "Do you want to enter another person?"
	repeat = raw_input('> ').lower()

print "Here are the contents of your people-book: "
print(Phonebook)
