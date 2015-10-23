# 10/22/2015
#
# This program creates a dictionary which has the terms from Exercise 41
# of Learning Python the Hard Way and modified definitions from Zeb's list
# and it makes a little reverse flashcard program to study them.
# 
# This time, instead of making an array and using a random element from
# my array to call from my dict, then deleting elements from the array,
# I modify the dict itself.



import random

terms = {
	'class': 'These are used (or "instantiated") to create objects. They have fields which represent quality the thing has, and methods which represent what the thing can do.',
	'object': 'This has two possible meanings 1. The most basic type of thing, 2. Any instance of some thing.',
	'instance': 'This is what you get when you tell Python to create a class.',
	'def': 'The syntax used to make a function inside of a class',
	'self': 'Inside the functions in a class, this is a variable for the instance or object being accessed.',
	'inheritance': 'The concept that one class can receive the traits of another class, much like genetics.',
	'composition': 'The concept that a class can have other classes as parts, much like how a car has wheels.',
	'attribute': 'A property classes have that are from composition, are usually variables.',
	'is-a': 'A phrase to say that something inherits from another class, as in a "salmon" **** "fish".',
	'has-a': 'A phrase to say that something is composed of other things or contains trait, as in "a salmon **** mouth."'
	}
	

while len(terms) != 0:
	print "Items_total at top: ", len(terms)  
	num = random.randrange(0, len(terms))
	print num
	print terms.values()[num], "\n"
	guess = raw_input('The corresponding term is: ').lower()
	print terms.keys()[num], "\n"
	
	if guess == terms.keys()[num]:
		print "Correct! \n"
		del terms[guess]
		
	else:
		print "Try again. \n"
		


