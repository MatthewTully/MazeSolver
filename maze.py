"""Create the Maze."""
from __future__ import annotations
from typing import TYPE_CHECKING
from time import sleep

from graphics import Cell

if TYPE_CHECKING:
    from window import Window

class Maze():
    """Hold Maze cells in 2D grid."""

    def __init__(self, x1:int, y1:int, num_rows: int, num_columns: int, cell_size_x: int, cell_size_y:int, win: Window=None) -> None:
        """Construct Maze class."""

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        """Create cells and populate _cells list."""
        row_x1 = self._x1
        while len(self._cells) < self._num_rows:
            row = []
            row_y1 = self._y1
            while len(row) < self._num_columns:
                row.append(Cell(row_x1, row_y1, row_x1+self._cell_size_x, row_y1+self._cell_size_y, self._win))
                row_y1 += self._cell_size_y
            row_x1 += self._cell_size_x
            self._cells.append(row)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    
    def _draw_cell(self, row_index: int, column_index: int) -> None:
        """Call draw cell on the cell at the provided index."""
        if self._win is None:
            return
        self._cells[row_index][column_index].draw()
        self._animate()
    
    def _animate(self) -> None:
        """Calls redraw and sleeps."""
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        if len(self._cells) == 0:
            return
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._animate()

        self._cells[-1][-1].has_right_wall = False
        self._cells[-1][-1].draw()
        self._animate()

