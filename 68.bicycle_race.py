# Bicyclist problem
# 11.16.15 GGuy

race_data = open("68.race_data.txt", "r") 
distance_data = open("68.distance_data.txt", "w")

for line in race_data:
	S, A, B = line.split(' ')
	S = float(S)
	A = float(A)
	B = float(B)

	print S, A, B

	x = S / (A + B)
	dist1 = A * x
	
	distance_data.write(str(dist1))
	distance_data.write(' ')


race_data.close()
distance_data.close()


