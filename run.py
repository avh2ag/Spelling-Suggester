
from data_processing.frequency_table import FrequencyTable

def main():
	table = FrequencyTable()
	#print table.get_frequency("123")
	table.import_words('word_frequency.csv')
	print "thank you" in table.words_by_length(9)

main()