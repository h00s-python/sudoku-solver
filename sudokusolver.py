class SudokuSolver:

	def __init__(self, sudoku):
		self.sudoku = sudoku
		self.i = 0

	def solve_backtrack(self):
		row, column = self.sudoku.find_empty()
		if row == None or column == None:
			return True

		for k in range(1,10):
			if self.sudoku.is_valid_number(k, row, column):
				self.sudoku.set_number_at(k, row, column)
				self.i = self.i + 1
				if self.solve_backtrack():
					return True
				self.sudoku.set_number_at(0, row, column)
		return False
