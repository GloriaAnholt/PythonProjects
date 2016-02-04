# Rodalind: Computing GC Content
# 11.30.15
# @totallygloria


in_file = open("gc.Computing GC Content.data.py", "r")
raw_string = in_file.read()
raw_string = raw_string.replace('\n', '')
raw_list = raw_string.split(">")
del raw_list[0]

#sting[">":"\n":1]

def build_strand_dicts(in_list):					
		
		strand_list = []
		
		for entry in in_list:
			title = ""
			strand = ""
			for char in entry:
				if char not in "ACGT":
					title += char	
				elif char != "R":
					strand += char
				length = len(strand)
			strand_list.append({"title": title, "strand": strand, "length": length})
		return strand_list
			
	
def most_cg_pairs(strand_list):

	strand_title = ""
	largest_count = 0
	percentage_val = 0
	
	for d in strand_list:
		current_strand = d["strand"]
		current_count = 0
		for base in current_strand:
			if base in "CG":
				current_count += 1
		print current_count
			
		if current_count > largest_count:
			largest_count = current_count
			strand_title = d["title"]
			percentage_val = float(largest_count * 100) / d["length"]		
	
	print strand_title, percentage_val
	

strand_list = build_strand_dicts(raw_list)

most_cg_pairs(strand_list)

