from cell import Cell
from pprint import pprint
import time
import random

class Maze:
	def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win
		if seed:
			random.seed(seed)

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0,0)
		self._reset_cells_visited()

	def _create_cells(self):
		self._cells = [ [Cell(self._win) for i in range(self._num_cols)] for j in range(self._num_rows) ]

		for i in range(self._num_rows):
			for j in range(self._num_cols):
				self._draw_cell(i , j)
				
	def _reset_cells_visited(self):
		for i in range(self._num_rows):
			for j in range(self._num_cols):
				self._cells[i][j].visited = False

	def _draw_cell(self, i, j):
		if self._win is None:
			return
		x1 = self._x1 + i * self._cell_size_x
		y1 = self._y1 + j * self._cell_size_y
		x2 = x1 + self._cell_size_x
		y2 = y1 + self._cell_size_y
		self._cells[i][j].draw(x1, y1, x2, y2)
		self._animate()
	
	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0, 0)
		self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
		self._draw_cell(self._num_rows - 1, self._num_cols - 1)

	def _break_walls_r(self, i, j):
		self._cells[i][j].visited = True
		while True:
			next_index_list = []

			#check left
			if i > 0 and not self._cells[i - 1][j].visited:
				next_index_list.append((i - 1, j))
			#check right
			if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
				next_index_list.append((i + 1, j))
			#check top
			if j > 0 and not self._cells[i][j - 1].visited:
				next_index_list.append((i, j - 1))
			#check bottom
			if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
				next_index_list.append((i, j + 1))

			#no cells to visit
			if len(next_index_list) == 0:
				self._draw_cell(i, j)
				return
			
			random_direction_index = random.randrange(len(next_index_list))
			next_index = next_index_list[random_direction_index]
			
			#right
			if next_index[0] == i + 1:
				self._cells[i][j].has_right_wall = False
				self._cells[i + 1][j].has_left_wall = False
			#left 
			if next_index[0] == i - 1:
				self._cells[i][j].has_left_wall = False
				self._cells[i - 1][j].has_right_wall = False
			#down 
			if next_index[1] == j + 1:
				self._cells[i][j].has_bottom_wall = False
				self._cells[i][j + 1].has_top_wall = False
			#up
			if next_index[1] == j - 1:
				self._cells[i][j].has_top_wall = False
				self._cells[i][j - 1].has_bottom_wall = False

			self._break_walls_r(next_index[0], next_index[1])
			
	def solve(self):
		return self._solve_r(0, 0)

	def _solve_r(self, i, j):
		self._animate()
		self._cells[i][j].visited = True
		current = self._cells[i][j]

		if i == self._num_rows - 1 and j == self._num_cols - 1:
			return True
		
		#left
		if i > 0 and not current.has_left_wall and not self._cells[i - 1][j].visited:
			current.draw_move(self._cells[i - 1][j])
			solver = self._solve_r(i - 1, j)
			if solver:
				return True
			current.draw_move(self._cells[i - 1][j], True)
		#right
		if i < self._num_rows - 1 and not current.has_right_wall and not self._cells[i + 1][j].visited:
			current.draw_move(self._cells[i + 1][j])
			solver = self._solve_r(i + 1, j)
			if solver:
				return True
			current.draw_move(self._cells[i + 1][j], True)
		#up
		if j > 0 and not current.has_top_wall and not self._cells[i][j - 1].visited:
			current.draw_move(self._cells[i][j - 1])
			solver = self._solve_r(i, j - 1)
			if solver:
				return True
			current.draw_move(self._cells[i][j - 1], True)
		#down
		if j < self._num_cols - 1 and not current.has_bottom_wall and not self._cells[i][j + 1].visited:
			current.draw_move(self._cells[i][j + 1])
			solver = self._solve_r(i, j + 1)
			if solver:
				return True
			current.draw_move(self._cells[i][j + 1], True)
		
		return False

	def _animate(self):
		if self._win is None:
			return
		self._win.redraw()
		time.sleep(0.015)
	
	def print_cells(self):
		pprint(self._cells)