
from data_processing.frequency_table import frequency_table

def main():
	table = frequency_table()
	#print table.get_frequency("123")
	table.import_words('word_frequency.csv')
	print table.get_frequency("stunned")

main()