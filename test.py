import unittest

from maze import Maze

class Test(unittest.TestCase):
	def test_maze_create_cells(self):
		rows = 10
		cols = 12
		maze = Maze(0, 0, rows, cols, 10, 10)
		self.assertEqual(len(maze._cells), rows)
		self.assertEqual(len(maze._cells[0]), cols)

if __name__ == "__main__":
	unittest.main()