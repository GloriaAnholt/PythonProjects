# 10/23/2015
#
# This program creates a dictionary which has the terms from Exercise 41
# of Learning Python the Hard Way and modified definitions from Zeb's list
# and it makes a little reverse flashcard program to study them.
# 
# Once again, this time turning the terms dict into a list of dicts.


import random
		

my_terms = {
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


my_list = []

for k, v in my_terms.items():
	my_list.append({"term": k, "definition": v})


class Deck(object):
	
	def __init__(self, terms):
		self.terms = terms

	def have_terms(self):
		if len(self.terms) > 0:
			return True
		else:
			return False

#this can be done in fewer lines -- fix it
	def random_card(self):
		num = random.randrange(0, len(self.terms))
		term = self.terms.keys()[num]
		definition = self.terms.values()[num]
		return (term, definition)
		
	def delete_card(self, guess):
		del self.terms[guess]
		
		
my_deck = Deck(my_terms)

while my_deck.have_terms():
	term, definition = my_deck.random_card()
	print definition
	guess = raw_input('The corresponding term is: ').lower()
	if guess == term:
		my_deck.delete_card(guess)
		print "Correct! \n"
	else:
		print "Try again. \n"

