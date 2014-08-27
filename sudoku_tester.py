from sudoku import Sudoku
from sudokusolver import SudokuSolver

sudoku = Sudoku()
sudoku.load_from_file('sudoku6.txt')

#print(sudoku.number_in_row(5, 5))
#print(sudoku.number_in_column(5,3))
#print(sudoku.number_in_cluster(4, 3, 4))

sudoku.print_grid()
solver = SudokuSolver(sudoku)
solver.solve_backtrack()
solver.sudoku.print_grid()
