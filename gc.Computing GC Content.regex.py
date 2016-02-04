# Rodalind: Computing GC Content
# 11.30.15
# @totallygloria

import re

in_file = open("gc.Computing GC Content.data.py", "r")
raw_dna = in_file.read()
raw_dna = raw_dna.replace('\n', '')


def build_strand_dicts(raw_data):					
		
	title = re.compile("Rosalind_[0-9]{4}")
	strand = re.compile(r"(?m)([CGAT]+)")
	titles = title.findall(raw_data)
	strands = strand.findall(raw_data)
	strand_dict = {}
	for i in range(len(titles)):
		strand_dict[titles[i]] = strands[i]
	print strand_dict	
	
def most_cg_pairs(strands):

	pass
	#largest_cg = max(strands.values()["cg_len"])
	#print largest_cg

build_strand_dicts(raw_dna)



