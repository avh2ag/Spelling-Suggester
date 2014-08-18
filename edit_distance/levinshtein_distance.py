"""
levinshtein_distance.py
Calculates the edit, or Levinshtein distance between two words
Inputs: 2 words
Outputs: the distance between them.
"""
from Grid import Grid #simplified instead of using numpy
def edit_distance(s1, s2):
	length_1 = len(s1)
	length_2 = len(s2)
	grid = Grid(length_2+1, length_1+1) #sets so that grid.get_value(len, len) is valid
	string_1 = s1.lower()
	string_2 = s2.lower()
	return levinshtein_distance(grid, string_1,string_2)

def levinshtein_distance(grid, s1, s2):
	s1_length = len(s1)
	s2_length = len(s2)
	if s1_length == 0:
		return s2_length
	if s2_length == 0:
		return s1_length
	for i in range(0, s2_length+1):
		grid.set_value(i, 0, i)
	for j in range(0, s1_length+1):
		grid.set_value(0, j, j)

	for i in range(1, s2_length+1):
		for j in range(1, s1_length+1):
		#	print i,j
			if s2[i-1] == s1[j-1]:
				prev_value = grid.get_value(i-1, j-1)
				grid.set_value(i, j, prev_value)
			else:
				substitution = grid.get_value(i-1, j-1) + 1
				insertion = grid.get_value(i, j-1) + 1
				deletion = grid.get_value(i-1, j) + 1
				minimum = min(substitution, insertion, deletion)				
				grid.set_value(i, j, minimum)
	return grid.get_value(s2_length, s1_length)

print edit_distance("kitten", "sitting")
