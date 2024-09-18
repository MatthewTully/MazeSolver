"""Create the Maze."""
from __future__ import annotations
from typing import TYPE_CHECKING
from time import sleep
import random

from graphics import Cell

if TYPE_CHECKING:
    from window import Window

class Maze():
    """Hold Maze cells in 2D grid."""

    def __init__(self, x1:int, y1:int, num_rows: int, num_columns: int, cell_size_x: int, cell_size_y:int, win: Window=None, seed: int=None) -> None:
        """Construct Maze class."""
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed != None:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        if num_columns is None or num_rows is None or num_rows <= 0 or num_columns <= 0:
            raise ValueError("Can not define maze with no rows or columns.")
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
        self._animate(delay=0.0001)
    
    def _animate(self, delay:float=0.5) -> None:
        """Calls redraw and sleeps."""
        if self._win is None:
            return
        self._win.redraw()
        sleep(delay)

    def _break_entrance_and_exit(self) -> None:
        """Break the entrance and exit walls."""
        if len(self._cells) == 0:
            return
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._animate()

        self._cells[-1][-1].has_right_wall = False
        self._cells[-1][-1]._maze_exit = True
        self._cells[-1][-1].draw()
        self._animate()

    def _break_walls_r(self, row_index: int, column_index: int) -> None:
        """Recursive function to break walls in the Maze."""        
        self._cells[row_index][column_index]._visited = True
        
        possible_dir = []

        if column_index > 0:
            above_cell = self._cells[row_index][column_index-1]
            if not above_cell._visited:
                possible_dir.append(("up", row_index, column_index-1))
        if row_index > 0:
            left_cell = self._cells[row_index-1][column_index]
            if not left_cell._visited:
                possible_dir.append(("left", row_index-1, column_index))
        if column_index < self._num_columns-1:
            below_cell = self._cells[row_index][column_index+1]
            if not below_cell._visited:
                possible_dir.append(("down", row_index, column_index+1))
        if row_index < self._num_rows-1:
            right_cell = self._cells[row_index+1][column_index]
            if not right_cell._visited:
                possible_dir.append(("right", row_index+1, column_index))
        if len(possible_dir) == 0:
            return
        while len(possible_dir) > 0:
            dir = random.randrange(0, len(possible_dir))
            next_cell: Cell = possible_dir[dir]
            possible_dir.pop(dir)
            if self._cells[next_cell[1]][next_cell[2]]._visited:
                continue
            if next_cell[0] == "up":
                self._cells[row_index][column_index].has_top_wall = False
                self._cells[next_cell[1]][next_cell[2]].has_bottom_wall = False
            if next_cell[0] == "left":
                self._cells[row_index][column_index].has_left_wall = False
                self._cells[next_cell[1]][next_cell[2]].has_right_wall = False
            if next_cell[0] == "down":
                self._cells[row_index][column_index].has_bottom_wall = False
                self._cells[next_cell[1]][next_cell[2]].has_top_wall = False
            if next_cell[0] == "right":
                self._cells[row_index][column_index].has_right_wall = False
                self._cells[next_cell[1]][next_cell[2]].has_left_wall = False
            self._cells[row_index][column_index].draw()
            self._cells[next_cell[1]][next_cell[2]].draw()
            self._animate(0.005)
            self._break_walls_r(next_cell[1], next_cell[2])

    def _reset_cells_visited(self) -> None:
        """Reset the visited flag for all cells."""
        for col in self._cells:
            for cell in col:
                cell._visited = False

    def solve(self) -> bool:
        """Attempt to solve the maze."""
        return self._solve_r(0,0)
    
    def _solve_r(self, row_index:int, column_index: int) -> bool:
        """Recursive method to solve the maze."""
        self._animate(0.1)
        current_cell = self._cells[row_index][column_index]
        current_cell._visited = True
        if current_cell._maze_exit:
            return True

        possible_dir = []
        if not current_cell.has_left_wall and (row_index != 0 and column_index != 0):
            left_cell = self._cells[row_index-1][column_index]
            if not left_cell._visited:
                possible_dir.append((row_index-1, column_index))
        if not current_cell.has_top_wall:
            above_cell = self._cells[row_index][column_index-1]
            if not above_cell._visited:
                possible_dir.append((row_index, column_index-1))
        if not current_cell.has_bottom_wall:
            below_cell = self._cells[row_index][column_index+1]
            if not below_cell._visited:
                possible_dir.append((row_index, column_index+1))
        if not current_cell.has_right_wall:
            right_cell = self._cells[row_index+1][column_index]
            if not right_cell._visited:
                possible_dir.append((row_index+1, column_index))
        for dir in possible_dir:
            to_cell = self._cells[dir[0]][dir[1]]
            current_cell.draw_move(to_cell)
            if self._solve_r(dir[0], dir[1]):
                return True
            current_cell.draw_move(to_cell, undo=True)
        return False
