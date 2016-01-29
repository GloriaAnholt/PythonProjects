# Exercise 40: Modules, Classes, and Objects
# 10/13/2015

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally 'round the family",
						"With a pocket full 'a shells"])
						

cecila = Song(["Making love in the afternoon", 
				"with Cecila, up in my bedroom.",
				"I get up to wash my face",
				"When I come back to bed, someone's taken my place."])
				
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

cecila.sing_me_a_song()


lyrics = ["I hear the sound of silence"]

sound_of_silence = Song(lyrics)

sound_of_silence.sing_me_a_song()
