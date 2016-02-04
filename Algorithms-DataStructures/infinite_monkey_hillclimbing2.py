# Algorithms and Data Structures: Intro
# Infinite Monkeys Theorem
# 12/19/15

import random, string


def generate_string():	# generates a random string 27 char long
	
	available_characters = "abcdefghijklmnopqrstuvwxyz "
	new_string = ''.join(random.choice(available_characters) for i in range(28))
	return new_string
	

def check_string(current_string):
	
	shakespear = "methinks it is like a weasel"
	match = 0
	correct_indices = []
	
	for i in range(28):
		if shakespear[i] == current_string[i]:
			match += 1
			correct_indices.append(i)
	
	match_percentage = float(match) / 28 * 100
	
	return current_string, match_percentage, correct_indices
	

def update_string(current_string, match_percentage, correct_indices):
	
	updated_string = ''
	
	for i in range(28):
		if i in correct_indices:
			updated_string += current_string[i]
		else:
			updated_string += random.choice("abcdefghijklmnopqrstuvwxyz ")
			
	return updated_string
	
	
def update_one(current_string, match_percentage, incorrect_indices):
	
	updated_string = current_string
	
	
	
	
	
starting = generate_string()

current_string, match_percentage, correct_indices = check_string(starting)

def do_the_thing(current_string, match_percentage, correct_indices):

	total_count = 0

	while match_percentage < 100:

		updated_string = update_string(current_string, match_percentage, correct_indices)
		current_string, match_percentage, correct_indices = check_string(updated_string)
		total_count += 1
		if total_count % 10 == 0:
			print current_string, match_percentage
			
	print current_string, match_percentage
	print "That took", total_count, "rounds to complete"

	
do_the_thing(current_string, match_percentage, correct_indices)
	

