"""
Grid.py
2d Array implementation instead of using numpy (for clarity)
"""

class Grid(object):
	def __init__(self, r=0, c=0):
		self.rows = r
		self.cols = c
		self.array = []
		for i in range(r):
			col_list = []
			for j in range(c):
				col_list.append(0) 
			self.array.append(col_list)


	def get_value(self, row, col):
		if self.out_of_bounds(row, col):
			return -1
		else:
			return self.array[row][col]

	def set_value(self, row, col, val):
		if self.out_of_bounds(row, col):
			return False
		else:
			self.array[row][col] = val
			return True

	def out_of_bounds(self, row, col):
		if row >= len(self.array) or row < 0:
			return True
		if col >= len(self.array[0]) or col < 0:
			return True
		return False

	def reset(self):
		for i in range(len(self.array)):
			for j in range(len(self.array[i])):
				self.array[i][j] = 0


