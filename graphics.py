"""Graphics Classes"""
from __future__ import annotations
from typing import TYPE_CHECKING

from tkinter import Canvas

if TYPE_CHECKING:
    from window import Window

class Point():
    """Point class."""

    def __init__(self, x_coord: int, y_coord:int) -> None:
        """Constructor for point class."""
        self.x_coord = x_coord
        self.y_coord = y_coord


class Line():
    """Line Class."""

    def __init__(self, point_a: Point, point_b: Point) -> None:
        """Constructor for Line class."""
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas: Canvas, fill_colour:str="black") -> None:
        """Draw a line on the canvas."""
        canvas.create_line(self.point_a.x_coord, self.point_a.y_coord, self.point_b.x_coord, self.point_b.y_coord, fill=fill_colour, width=2)
        

class Cell():
    """Cell Class."""

    def __init__(self, x1:int, y1:int, x2:int, y2:int, win: Window=None, wall_colour:str="black") -> None:
        "Construct a basic cell."
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self._wall_colour = wall_colour
        self._visited = False
        self._maze_exit = False

    def _determine_wall_colour(self, wall_exists: bool) -> str:
        """Checks if wall exists and returns Colour."""
        if wall_exists:
            return self._wall_colour
        return self._win.background_colour
    
    def draw(self) -> None:
        "Draw Cell to canvas."
        if self._win is None:
            return
        
        point_a = Point(self._x1, self._y1)
        point_b = Point(self._x1, self._y2)
        self._win.draw_line(Line(point_a, point_b), self._determine_wall_colour(self.has_left_wall))
        
        point_a = Point(self._x2, self._y1)
        point_b = Point(self._x2, self._y2)
        self._win.draw_line(Line(point_a, point_b), self._determine_wall_colour(self.has_right_wall))

        point_a = Point(self._x1, self._y1)
        point_b = Point(self._x2, self._y1)
        self._win.draw_line(Line(point_a, point_b), self._determine_wall_colour(self.has_top_wall))

        point_a = Point(self._x1, self._y2)
        point_b = Point(self._x2, self._y2)
        self._win.draw_line(Line(point_a, point_b), self._determine_wall_colour(self.has_bottom_wall))

    def get_centre(self) -> Point:
        """Return the center of the cell."""
        return Point(x_coord=(max(self._x1, self._x2)+min(self._x1, self._x2))/2,
                     y_coord=(max(self._y1, self._y2)+min(self._y1, self._y2))/2)
    
    def draw_move(self, to_cell: Cell, undo:bool=False):
        """Plot movement between cells."""
        line_colour = "red"
        if undo is True:
            line_colour = "grey"
        
        self._win.draw_line(Line(self.get_centre(), to_cell.get_centre()), line_colour)
        
