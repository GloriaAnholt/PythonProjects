# Algorithms and Data Structures: Intro
# Infinite Monkeys Theorem
# 12/19/15

import random, string

global starting_string 
starting_string = generate_string()
global correct_indices 
correct_indices = []


def generate_string():	# generates a random string 27 char long
	
	available_characters = "abcdefghijklmnopqrstuvwxyz "
	new_string = ''.join(random.choice(available_characters) for i in range(27))
	return new_string


def update_string(correct_indices, old_string):	# updates string, keeps correct letters
	
	available_characters = "abcdefghijklmnopqrstuvwxyz "
	corrected_string = ''
	
	for i in range(27):
		if i in correct_indices:
			corrected_string.append(old_string[i])
		else:
			corrected_string.append(''.join(random.choice(available_characters))

	print corrected_string


def score_string(random_string, correct_indices):		# scores string based on how close it is
	
	shakespeare = "methinks it is like a weasel"
	match = 0
	
	for i in range(27):
		if shakespeare[i] == random_string[i]:
			match += 1
			correct_indices.append(i)
	
	percent_match = float(match) / 27 * 100
		
	print (percent_match, correct_indices)
	
	
def string_checker():	# calls the other two, if 100%, we're done. Print every 1000th try and best string so far
	
	highest_match = 0
	total_calls = 0
	percentage_match = score_string(starting_string)
	current_string = starting_string
	
	while percentage_match < 100.0:
	
		updated_string = update_string(correct_indices, current_string)
		percentage_match, correct_indices = score_string(current_string)
		if percentage_match > highest_match:
			highest_match = percentage_match
			print current_string, percentage_match
		total_calls += 1
		if total_calls % 1000 == 0:
			print current_string, total_calls
		
	print "loop completed at %d calls" % (total_calls)



