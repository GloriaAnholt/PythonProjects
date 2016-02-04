# Rosalinda Python Village: 6 Dictionaries
# 11/20/15 GGuy


'''
go through one word at a time
compare word to key in dict
if not in dict, add as key with value 1
else change the value to increment by one
'''

sample = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
results = {}
new_list = []

def split_sample(text):
	new_list = text.split(' ')
	return new_list
	
def check_word(my_list):
	global results
	for word in my_list:
		if word in results:
			results[word] += 1
		else:
			results[word] = 1 



new_list = split_sample(sample)
check_word(new_list)


for key, value in results.items():
    print key
    print value
