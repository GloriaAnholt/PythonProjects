# 10/26/2015
#
# This program creates a dictionary which has the terms from Exercise 41
# of Learning Python the Hard Way and modified definitions from Zeb's list
# and it makes a little reverse flashcard program to study them.
# 
# Once again, this creating my list of dicts from a CSV file I open. 
# It also has a list of dicts, shuffles it, then pops the dict out of the
# list if the user guesses the correct term/def.


import random		


class Deck(object):
	
	def __init__(self, terms):
		self.terms = terms

	def have_terms(self):
		if len(self.terms) > 0:
			return True
		else:
			return False

	def random_card(self):
		random.shuffle(self.terms)
		return self.terms[-1]
		
	def delete_card(self):
		self.terms.pop()
		
		

def create_list():
	print "What file would you like to open?"
	my_file = raw_input("> ")
	my_text = open(my_file)
	my_list = []
	for line in my_text.readlines():
		k, v = line.split(',')
		my_list.append({"term": k, "definition": v})
	return my_list



my_list = create_list()
my_deck = Deck(my_list)

print "Which side do you want to practice? Terms or definitions?"
set_side = raw_input('> ').lower()

while True:
	if set_side == "terms" or set_side == "definitions":
		break
	else:
		print "Please select 'terms' or 'definitions'"
		set_side = raw_input('> ').lower()



while my_deck.have_terms():
	current_card = my_deck.random_card()
	if set_side == 'terms':
		print current_card['term']
		guess = raw_input('The corresponding definition is: ').lower()
		if guess == current_card['definition']:
			print "Correct! \n"
			my_deck.delete_card()
		else:
			print "Incorrect. \n"
	elif set_side == 'definitions':
		print current_card['definition']
		guess = raw_input('The corresponding terms is: ').lower()
		if guess == current_card['term']:
			print "Correct! \n"
			my_deck.delete_card()
		else:
			print "Incorrect. \n"

		


