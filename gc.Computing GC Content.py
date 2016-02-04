# Rodalind: Computing GC Content
# 11.30.15


in_file = open("dna.Computing GC Content.data.py", "r")
strand_dict = {"title": "", "strand": ""}
strand_list = []

for line in in_file.readlines():
	if line[0] == ">":
		strand_dict["title"] = line.rstrip('\n')
		strand_list.append(strand_dict)
	#next_line = in_file.readline()
	#print next_line
		#strand_dict["strand"] = line.rstrip('\n'))
		
			
for i in strand_list:
	for title in strand_dict:
		print strand_dict["title"]
		print strand_dict["strand"]

