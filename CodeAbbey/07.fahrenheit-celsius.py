# CodeAbbey: #7 Fahrenheit to Celsius
# 12.30.2015
# @totallygloria

in_temps = open('07.fahrenheit-celsius.data.txt')
f_data = in_temps.read()
f_temps = f_data.split()


def f_to_c_converter(farens):
	c_temps = []
	
	for temp in farens:
		f = float(temp)
		c = (f-32)*5/9
		c_temps.append(int(round(c)))
	
	return c_temps
	
c_temps = f_to_c_converter(f_temps)

for temp in c_temps:
	print temp,
