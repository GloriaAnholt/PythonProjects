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

print "Which side do you want to practice? Type 'term' or 'definition'"
set_side = raw_input('> ').lower()

while set_side != 'term' and set_side != 'definition':
	print "Please choose 'term' or 'definition'"
	set_side = raw_input('> ').lower()
	
if set_side == 'term':
	other_side = 'definition'
elif set_side == 'definition':
	other_side = 'term'


# for each card in this deck, do stuff

while my_deck.have_terms():
	current_card = my_deck.random_card()
	print current_card[set_side]
	guess = raw_input('The corresponding definition is: ').lower()
	if guess == current_card[other_side]:
		print "Correct! \n"
		my_deck.delete_card()
	else:
		print "Incorrect. \n"


		


