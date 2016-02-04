# Rodalind: Computing GC Content
# 11.30.15
# @totallygloria

import re

in_file = open("gc.Computing GC Content.data.py", "r")
raw_data = in_file.read()
raw_data = raw_data.replace('\n', '')

def build_strand_dicts(raw_data):					

	massaged_data = re.findall('>(Rosalind_[0-9]{4})([CGAT]+)', raw_data)
	strand_list = []
	for k,v in massaged_data:
		strand_len = len(v)
		content = 0
		for base in v:
			if base in "CG":
				content += 1
		strand_list.append({
							"title": k, "strand": v, 
							"length": strand_len, "cg content": content})			
	return strand_list
	
def most_cg_pairs(strands):
	
	pass



strand_dict = build_strand_dicts(raw_data)

for d in strand_dict:
	print d

