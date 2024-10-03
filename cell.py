from point import Point
from line import Line
from enum import Enum

class LineColor(Enum):
	BLACK = 1
	WHITE = 0

class Cell:
	def __init__(self, win=None):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = None
		self._x2 = None
		self._y1 = None
		self._y2 = None
		self.visited = False
		self._win = win

	def __repr__(self):
		return(f"Cell([{int(self.has_left_wall)}:{int(self.has_top_wall)}:{int(self.has_right_wall)}:{int(self.has_bottom_wall)}],"
		 + f"({self._x1}, {self._y1}) -> ({self._x2}, {self._y2})")

	def draw(self, x1, y1, x2, y2):
		if self._win is None:
			return

		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2

		tl_corner = Point(x1, y1) 
		tr_corner = Point(x2, y1)
		bl_corner = Point(x1, y2)
		br_corner = Point(x2, y2)

		
		self._win.draw_line(Line(bl_corner, tl_corner), LineColor(int(self.has_left_wall)).name)
		
		self._win.draw_line(Line(tl_corner, tr_corner), LineColor(int(self.has_top_wall)).name)
		
		self._win.draw_line(Line(tr_corner, br_corner), LineColor(int(self.has_right_wall)).name)
	
		self._win.draw_line(Line(br_corner, bl_corner), LineColor(int(self.has_bottom_wall)).name)
		
	def draw_move(self, to_cell, undo=False):
		if self._win is None:
			return
		if undo:
			color = "gray"
		else:
			color = "red"
		self._win.draw_line(Line(self.calculate_center(), to_cell.calculate_center()), color)

	def calculate_center(self):
		return Point(
			(self._x1 + self._x2) // 2,
			(self._y1 + self._y2) // 2 
		)