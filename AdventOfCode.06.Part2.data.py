# Advent Calendar of Code: 06, Part 2
# 12.15.15
# @totallygloria

import re




def create_instructions():

	in_file = open("advent.06.data.py", "r")
	num = re.compile(r'(?P<x1>[0-9]{1,3}),(?P<y1>[0-9]{1,3}).* (?P<x2>[0-9]{1,3}),(?P<y2>[0-9]{1,3})')
	instructions = []
	status = 0     # let's try this with -1: off, 1: on, 2: toggle
	
	for line in in_file:
		nums = re.search(num, line)
		x1, y1 = int(nums.group('x1')), int(nums.group('y1'))
		x2, y2 = int(nums.group('x2')), int(nums.group('y2'))
		
		if "turn off" in line:
			intensity = -1
		elif "turn on" in line:
			intensity = 1
		elif "toggle" in line:
			intensity = 2
		else:
			print "Something went wrong here."

		instructions.append([intensity, x1, y1, x2, y2])
	
	return instructions


def initialize_grid():

	grid = [[0] * 1000 for i in range(1000)]
	
	return grid


	
def toggle_lights(inst, grid):

	
	for line in inst:
		intensity, x1, y1, x2, y2 = line[0], line[1], line[2], line[3], line[4]
						
		for row in range(y1,y2+1):
			for light in range(x1,x2+1):
				if intensity == -1 and grid[row][light] > 0:	
					grid[row][light] -= 1	# subtract 1 from intensity of light in grid
				if intensity == 1:
					grid[row][light] += 1	# add 1 to intensity of light in grid
				if intensity == 2:	
					grid[row][light] += 2	# add 2 to intensity of light in grid
			
	return grid


def calculate_lights(grid):
	
	light_count = 0
	
	for line in grid:
		for light in line:
			if light > 0:
				light_count += light
	
	return light_count


instructions = create_instructions()
grid = initialize_grid()

print calculate_lights(toggle_lights(instructions, grid))
	
