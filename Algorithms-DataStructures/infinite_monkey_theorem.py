# Algorithms and Data Structures: Intro
# Infinite Monkeys Theorem
# 12/19/15

import random, string


def generate_string():	# generates a random string 27 char long
	
	available_characters = "abcdefghijklmnopqrstuvwxyz "
	new_string = ''.join(random.choice(available_characters) for i in range(27))
	return new_string


def score_string(random_string):		# scores string based on how close it is
	
	shakespear = "methinks it is like a weasel"
	percent_match = 0
	
	for i in range(27):
		if shakespear[i] == random_string[i]:
			percent_match += 1
		
	return float(percent_match) / 27 * 100
	
	
def string_checker():	# calls the other two, if 100%, we're done. Print every 1000th try and best string so far
	
	highest_match = 0
	total_calls = 0
	percentage_match = 0
	
	while percentage_match < 100.0:
	
		new_string = generate_string()
		percentage_match = score_string(new_string)
		if percentage_match > highest_match:
			highest_match = percentage_match
			print new_string, percentage_match
		total_calls += 1
		if total_calls % 1000 == 0:
			print new_string, total_calls
		
	print "loop completed at %d calls" % (total_calls)


string_checker()
