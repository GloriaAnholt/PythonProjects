# Rodalind: Computing GC Content
# 12.04.15
# @totallygloria

import re
import collections

in_file = open("gc.Computing GC Content.data.py", "r")
raw_data = in_file.read()
raw_data = raw_data.replace('\n', '')

def build_strand_dicts(raw_data):					

	massaged_data = re.findall('>(?P<title>Rosalind_[0-9]{4})(?P<bases>[ACGT+]+)', raw_data)
	strand_list = []
	for x,y in massaged_data:
		strand_list.append({"title": x, "bases": y})			
	return strand_list
	
def most_cg_pairs(strands):
	
	# This doesn't work because it sums ALL of the letters together
	# but it otherwise an interesting idea
	'''
	test = collections.Counter()
	for d in strands:
		test.update(d["strand"])
	for letter, count in test.most_common(4):
		print '%s: %7d' % (letter, count)
	'''
	# Trying to work out the logic in a loop to see if I can escape
	# using loops. Can't so far.
	'''
	content = []
	for d in strands:
		counter = 0
		total = 0
		for base in d["strand"]:
			if base:
				total += 1
			if base in "CG":
				counter += 1
		content.append([total, counter])
	print content
	'''
	# Still using for loops, not they're a lot less clear. Trying to use
	# .count and max(), but haven't really figured it out. 
	'''
	test = []
	for d in strands:
		test.append([d["strand"].count(""), d["strand"].count("C") + d["strand"].count("G")])
	for i in test:
		print (float(i[1])/float(i[0]))
	'''
	# Trying making a letter-counting dictionary for each dictionary
	# It works, but it looks like a total PITA to tabulate totals and
	# do my division. Still not happy.
	'''	
	new_dict = {}
	
	for d in strands:
		title = d["title"]
		print title
		new_dict[title]= collections.Counter(d["bases"])	
	return new_dict	
	'''
	
	
	
#strand_list = build_strand_dicts(raw_data)
#most_cg_pairs(strand_list)

