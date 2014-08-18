"""
test_frequency_table.py 
Tests methods from frequency_table.py
"""

from frequency_table import FrequencyTable

def test_add_word_both_args():
	table = FrequencyTable()
	word = "abc"
	frequency = 2
	table.add_word(word, frequency)
	assert 3 in table.map.keys()
	assert table.map[3][word] == 2
	assert 2 not in table.map.keys()
	assert "abc" not in table.map.keys()

def test_add_word_one_arg():
	table = FrequencyTable()
	word = "abc"
	table.add_word(word)
	assert 3 in table.map.keys()
	assert table.map[3][word] == 1

def test_get_frequency():
	table = FrequencyTable()
	word = "abc"
	frequency = 2
	table.add_word(word, frequency)
	assert table.get_frequency(word) == 2
	assert table.get_frequency('a') == 0
	assert table.get_frequency(4) == 0

def test_import_words():
	table = FrequencyTable()
	valid_file = "C:\Users\Alex\Documents\GitHub\Spelling-Suggester\word_frequency.csv"
	invalid_file = ""
	assert table.import_words(valid_file)
	assert not table.import_words(invalid_file)

def test_words_by_length():
	table = FrequencyTable()
	table.add_word("a")
	table.add_word("b")
	table.add_word("ab")
	assert table.words_by_length(1) == {'a' : 1, 'b' : 1}
	assert table.words_by_length(2) == {'ab' : 1}
	assert table.words_by_length(3) == {}
	