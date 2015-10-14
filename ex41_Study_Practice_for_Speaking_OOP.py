# Exercise 41: Learning To Speak Obect Orientated
# 10/14/2015

# This program creates a dictionary which has the terms from Exercise 41
# of Learning Python the Hard Way and modified definitions from Zeb's list
# and it makes a little reverse flashcard program to study them.
#
# It creates a list the same length as the number of items in the dict,
# shuffles the list, grabs the last element and prints the value, 
# if you guess the corresponding key correctly, it pops the last element 
# and repeats until the list is empty. If you miss the word, it simply 
# shuffles and repeats.
#
# I didn't do any clever text editing, but I did set the user input to 
# lowercase to match the dict so you're not penalized if you caps the term.

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
	
	
items_total = range(0, len(terms))

while len(items_total) != 0:
	random.shuffle(items_total)
	i = items_total[-1]
	print terms.values()[i] 
	guess = raw_input('Term: ').lower()

	if guess == terms.keys()[i]:
		items_total.pop()
		print "Correct! \n"
	else:
		print "Try again. \n"
		
