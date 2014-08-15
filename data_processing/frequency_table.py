"""
frequency_table.py
Maps words to their search frequency
Inputs: 
List of words and their associated frequencies
"""

class frequency_table(object):
	def __init__(self):
		self.map = {}
		self.map_keys = []


	def add_word(self, word, frequency):
		word_len = len(word)
		mapping = (word, frequency)
		if word_len in self.map_keys:
			self.map[word_len].append(mapping)
		else:
			self.map_keys.append(word_len)
			self.map[word_len] = []
			self.map[word_len].append(mapping)
		#print self.map

	def get_frequency(self, word):
		word_len = len(word)
		if word_len in self.map_keys:
			for word_map in self.map[word_len]:
				if word == word_map[0]:
					return word_map[1]
		else:
			return 0

	def import_words(self, filename):
		file_object = open(filename, 'rb')
		line = file_object.readline()
		while line:
			info = line.split(',')
			word = info[0]
			frequency = info[1]
			self.add_word(word, frequency)
			line = file_object.readline()
		file_object.close()
				#frequency = info[1]
				#print word, frequency
