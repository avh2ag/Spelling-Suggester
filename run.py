
from data_processing.frequency_table import FrequencyTable

def main():
	table = frequency_table()
	#print table.get_frequency("123")
	table.import_words('word_frequency.csv')
	print table.words_by_length(2)

main()