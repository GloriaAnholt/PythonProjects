# Rodalind: Computing GC Content
# 11.30.15


in_file = open("gc.Computing GC Content.data.py", "r")



def build_strand_dict(in_file):

	strand_list = []

	for line in in_file:
		title, strand = line.split('>')
		if line[0] == ">":	
			title = line.rstrip('\n')
			next_line = line.next()
			strand = next_line.rstrip("\n")
			strand_list.append({"title": title, "strand": strand})
	return strand_list

strand_list = build_strand_dict(in_file)	
	
for i in strand_list:
	print i
		
	
def count_cg_pairs(strand_list):

	dict_title = ""

	for d in strand_list:
		current_count = 0
		largest_count = 0
		percentage_val = 0
		current_strand = d["strand"]
		strand_length = len(current_strand)
		for base in current_strand:
			if base in "CG":
				current_count += 1
		if current_count > largest_count:
			largest_count = current_count
			dict_title = d["title"]
			percentage_val = float(largest_count * 100) / float(strand_length)		
	
	print dict_title, percentage_val
		


count_cg_pairs(strand_list)
