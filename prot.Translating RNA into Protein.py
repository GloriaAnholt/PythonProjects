# PROT: Translating RNA into Protein
# 12.01.15
# @totallygloria

'''
function to read through the file and slice three-letters into dna 
and one letter into amino acid in a dictionary, append to end of list

function to scan three characters at a time, match to a dna, and then 
append amino acid to a list (the protein created)
'''

in_file = open("prot.Translating RNA into Protein.data.py", "r")

def data_massage(file_in):
	
	rna_data = in_file.read()
	rna_data = rna_data.replace("\n", "").replace(" ", "")
	rna_data = rna_data[::-1]
	rna_list = list(rna_data)
	return rna_list

def rna_amino_dict(rna_info):
	
	rna = ""
	ra_dict = {}
	ra_list = []
	
	for char in range(len(rna_info)):
		if char == "p":
			#do things
			pass
		else:
			amino = rna_info.pop()
			for i in range(3):
				rna += rna_info.pop()
			ra_dict = {"rna": rna, "amino": amino}
			ra_list.append(ra_dict)
	return ra_list
	
rna_reversed = data_massage(in_file)

rna_amino = rna_amino_dict(rna_reversed)

for k,v in rna_amino:
	print k
	print v
