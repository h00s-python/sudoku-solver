class Sudoku:

	def __init__(self):
		self.grid = [[0 for _ in range(9)] for _ in range(9)]

	def load_from_file(self, file_name):
		with open(file_name, 'r') as f:
			self.grid = [[int(number) for number in line.strip().split(',')] for line in f.readlines()]

	def number_in_row(self, number, row):
		if number in self.grid[row]:
			return True
		return False

	def number_in_column(self, number, column):
		if number in [line[column] for line in self.grid]:
			return True
		return False

	def number_in_cluster(self, number, row, column):
		if number in [number for cluster in [[number for number in line[column//3 * 3:column//3 * 3 + 3]] for line in self.grid[row//3 * 3:row//3 * 3 + 3]] for number in cluster]:
			return True
		return False

	def number_at(self, row, column):
		return self.grid[row][column]

	def find_empty(self):
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] == 0:
					return i, j
		return None, None

	def is_valid(self):
		for row in self.grid:
			if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
				return False

		for i in range(9):
			column = [line[i] for line in self.grid]
			if sorted(column) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
				return False

		for i in range(3):
			for j in range(3):
				temp = self.grid[i*3][j*3:j*3 + 3] + self.grid[i*3 + 1][j*3:j*3 + 3] + self.grid[i*3 + 2][j*3:j*3 + 3]
				if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
					return False

		return True

	def is_valid_number(self, number, row, column):
		if not (self.number_in_row(number, row) or self.number_in_column(number, column) or self.number_in_cluster(number, row, column)):
			return True
		return False

	def set_number_at(self, number, row, column):
		self.grid[row][column] = number

	def print_grid(self):
		""" Prints a sudoku thingy nicely. """
		print("+-------+-------+-------+")
		for i in range(9):
			print("| {} {} {} | {} {} {} | {} {} {} |".format(*self.grid[i]).replace("0"," "))
			if (i + 1) % 3 == 0:
				print("+-------+-------+-------+")
