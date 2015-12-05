# Advent Calendar of Code: 02 
# 12.04.15
# @totallygloria

import re

in_file = open("advent.02.data.py", "r")
data = in_file.read()



num = re.compile('(?P<l>[0-9]+)x(?P<w>[0-9]+)x(?P<h>[0-9]+)', re.M)
box_tuple = re.findall(num, data)
box_list = [list(box) for box in box_tuple]



def calculate_paper(box_list):

	paper = 0

	for box in box_list:
		l, w, h = int(box[0]), int(box[1]), int(box[2])
		side1 = l*w 
		side2 = w*h 
		side3 = h*l
		paper += ((side1 + side2 + side3)*2 + min(side1, side2, side3))

	return paper
	

def calculate_ribbon(box_list):
	
	sorted_boxes = [sorted(x) for x in box_list]
	print sorted_boxes
		
	
		
calculate_ribbon(box_list)
