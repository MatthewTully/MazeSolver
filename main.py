"""Main entry for Maze solver."""
from window import Window
from maze import Maze
from recursion_limit import RecursionLimit

limit = RecursionLimit(2000)

def main():
    """Start the application."""
    num_row = 50
    num_columns = 50
    margin = 50
    screen_width = 1920
    screen_height = 1080
    cell_size_x = (screen_width - (2 * margin)) / num_row
    cell_size_y = (screen_height - (2 * margin)) / num_columns

    win = Window(screen_width,screen_height)
    maze = Maze(margin, margin, num_row, num_columns, cell_size_x, cell_size_y, win)
    
    maze.solve()
    win.wait_for_close()


if "__main__" == __name__:
    with limit:
        main()