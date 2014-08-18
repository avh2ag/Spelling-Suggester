"""
frequency_table.py
Maps words to their search frequency
Inputs: 
List of words and their associated frequencies
"""

class FrequencyTable(object):
	def __init__(self):
		self.map = {}
		
	def add_word(self, word, frequency=1):
		word_len = len(word)
		mapping = (word, frequency)
		if word_len in self.map.keys():
			self.map[word_len][word] = frequency
		else:
			self.map[word_len] = {}
			self.map[word_len][word] = frequency
		
	def get_frequency(self, word):
		try:
			word_len = len(word)
			if word_len in self.map.keys():
				eligible = self.map[word_len]
				if word in eligible.keys():
					return eligible[word]
			else:
				return 0
		except Exception as e:
			print("Key error")
			return 0 

	def import_words(self, filename):
		try:
			file_object = open(filename, 'rb')
			line = file_object.readline()
			while line:
				info = line.split(',')
				word = info[0]
				frequency = info[1]
				self.add_word(word, frequency)
				line = file_object.readline().strip()
			file_object.close()
			return True
		except Exception as e:
			print("Problem reading file", e)
			return False

	def words_by_length(self, length):
		if length in self.map.keys():
			return self.map[length]
		else:
			return {}