
from data_processing.frequency_table import FrequencyTable
from edit_distance.levinshtein_distance import *

def main():
	table = FrequencyTable()
	#print table.get_frequency("123")
	table.import_words('word_frequency.csv')
	#print get_suggestions("badmiton", table)
#	print edit_distance("baleout", "bail out")
	query_file = open('mispelled_queries.csv', 'rb')
	output = open('suggestions.txt', 'w')
	while True:
		line = query_file.readline().strip()
		if not line:
			break
		else:
			suggestions = get_suggestions(line, table)
			#print line.strip(), suggestions
			output_string = "* {0} {1} \n".format(line, suggestions)
		#	print(output_string)
			output.write(output_string)
	query_file.close()
	
	#print get_suggestions("baleout", table)
	output.close()

def get_suggestions(input, table):
	input_length = len(input)
	raw_suggestions = []
	lengths = []
	if input_length == 0:
		return []
	if input_length == 1:
		lengths = [1, 2, 3]
	else:
		lengths.append(input_length+1)
		lengths.append(input_length+2)
		lengths.append(input_length-1)
		lengths.append(input_length)

	for length in lengths:
		dictionary = table.words_by_length(length)
		for word in dictionary.keys():
			distance = edit_distance(word, input)
			if distance < 3:
				raw_suggestions.append({"word": word, "frequency": dictionary[word], "distance": distance})
	suggestions = rank_suggestions(raw_suggestions)
	return suggestions

def rank_suggestions(raw_suggestions):
	in_order = sorted(raw_suggestions, key = lambda x: (x["distance"], -1*x["frequency"]))
	suggestions = []
	for i in in_order:
		suggestions.append(i["word"])
	return suggestions


	

main()

