# Advent Calendar of Code: 02 
# 12.04.15
# @totallygloria

import re



def create_box_list():
	
	in_file = open("advent.02.data.py", "r")
	box_list = []
	
	for line in in_file:
		box_list.append(sorted([int(x) for x in line.split('x')]))
	
	return box_list


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

	total_ribbon = 0
	
	for box in box_list:
		a, b, c = int(box[0]), int(box[1]), int(box[2])
		ribbon = 2*(a+b)
		bow = a*b*c
		total_ribbon += ribbon + bow
	
	print total_ribbon
	
		
		
	
box_list = create_box_list()
calculate_ribbon(box_list)

