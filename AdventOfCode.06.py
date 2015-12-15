# Advent Calendar of Code: 06 
# 12.15.15
# @totallygloria

import re




def create_instructions():

	in_file = open("advent.06.data.py", "r")
	num = re.compile(r'(?P<x1>[0-9]{1,3}),(?P<y1>[0-9]{1,3}).* (?P<x2>[0-9]{1,3}),(?P<y2>[0-9]{1,3})')
	instructions = []
	status = 0     # let's try this with 0: off, 1: on, 2: toggle
	
	for line in in_file:
		nums = re.search(num, line)
		x1, y1 = int(nums.group('x1')), int(nums.group('y1'))
		x2, y2 = int(nums.group('x2')), int(nums.group('y2'))
		
		if "turn off" in line:
			status = 0
		elif "turn on" in line:
			status = 1
		elif "toggle" in line:
			status = 2
		else:
			print "Something went wrong here."

		instructions.append([status, x1, y1, x2, y2])
	
	return instructions


def initialize_grid():

	grid = [[0] * 1000 for i in range(1000)]
	
	return grid


	
def toggle_lights(inst, grid):

	
	for line in inst:
		status, x1, y1, x2, y2 = line[0], line[1], line[2], line[3], line[4]
						
		for row in range(y1,y2+1):
			for light in range(x1,x2+1):
				if status == 0:				# turn off lights in grid
					grid[row][light] = 0
				if status == 1:				# turn on lights in grid
					grid[row][light] = 1
				if status == 2:				# toggle lights in grid
					if grid[row][light] == 0:
						grid[row][light] = 1
					else:
						grid[row][light] = 0	
			
	return grid


def calculate_lights(grid):
	
	light_count = 0
	
	for line in grid:
		for light in line:
			if light == 1:
				light_count += 1
	
	return light_count


instructions = create_instructions()
grid = initialize_grid()

print calculate_lights(toggle_lights(instructions, grid))
	
