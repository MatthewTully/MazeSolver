"""Unit tests."""

import unittest
import unittest.main

from maze import Maze

class Tests(unittest.TestCase):

    def test_maze_constructor(self):
        maze = Maze(1,2,3,4,5,6,None)
        self.assertEqual(maze._x1, 1)
        self.assertEqual(maze._y1, 2)
        self.assertEqual(maze._num_rows, 3)
        self.assertEqual(maze._num_columns, 4)
        self.assertEqual(maze._cell_size_x, 5)
        self.assertEqual(maze._cell_size_y, 6)
        self.assertIsNone(maze._win)

    def test_maze_create_cells(self):
        num_col = 5
        num_row = 5
        m1 = Maze(0,0,num_columns=num_col, num_rows=num_row, cell_size_x=10, cell_size_y=10)
        self.assertEqual(len(m1._cells), num_row)
        self.assertEqual(len(m1._cells[0]), num_col)

        num_col = 0
        num_row = 0
        m2 = Maze(0,0,num_columns=num_col, num_rows=num_row, cell_size_x=10, cell_size_y=10)
        self.assertListEqual(m2._cells, [])
        
    def test_maze_entrance_and_exit(self):
        num_row = 12
        num_columns = 16
        margin = 50
        screen_width = 800
        screen_height = 600
        cell_size_x = (screen_width - (2 * margin)) / num_row
        cell_size_y = (screen_height - (2 * margin)) / num_columns

        maze = Maze(margin, margin, num_row, num_columns, cell_size_x, cell_size_y, None)
        entrance_cell = maze._cells[0][0]
        self.assertFalse(entrance_cell.has_left_wall)
        exit_cell = maze._cells[-1][-1]
        self.assertFalse(exit_cell.has_right_wall)


if __name__ == "__main__":
    unittest.main()