# Advent Calendar of Code: 07
# 12.16.15
# @totallygloria

import re




def initialize_wirelist():

	in_file = open("advent.07.data.py", "r")
	find_wires = re.compile(r'(?P<wire1>[a-z]{1,2}).*(?P<wire2>[a-z]{1,2}) -> (?P<wire3>[a-z]{1,2})')
	wire_set = set()
	
	for line in in_file:
		wires = re.search(find_wires, line)
		if wires != None:
			w1, w2, w3 = wires.group('wire1'), wires.group('wire2'), wires.group('wire3')
			wire_set.add(w1)
			wire_set.add(w2)
			wire_set.add(w3)
		
	wires = dict.fromkeys(wire_set)
	
	return wires
	

def set_starting_values(wires):

	in_file = open("advent.07.data.py", "r")
	find_set_wires = re.compile(r'(?P<value>[0-9]{1,5}) -> (?P<wire>[a-z]*)')
	
	for line in in_file:
		start_cond = re.match(find_set_wires, line)
		if start_cond != None:
			val, wire = start_cond.group('value'), start_cond.group('wire')
			wires[wire] = int(val)
		
	return wires


starting_wire_values = set_starting_values(initialize_wirelist())
print starting_wire_values
