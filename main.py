"""Main entry for Maze solver."""
from window import Window
from maze import Maze


def main():
    """Start the application."""

    num_row = 12
    num_columns = 16
    margin = 50
    screen_width = 800
    screen_height = 600
    cell_size_x = (screen_width - (2 * margin)) / num_row
    cell_size_y = (screen_height - (2 * margin)) / num_columns

    win = Window(screen_width,screen_height)
    maze = Maze(margin, margin, num_row, num_columns, cell_size_x, cell_size_y, win)

    win.wait_for_close()


if "__main__" == __name__:
    main()