"""Window class definition."""
from tkinter import Tk, BOTH, Canvas
from graphics import Line

class Window():
    """Window class."""
    def __init__(self, width:int, height:int, background_colour: str="white") -> None:
        """Window Constructor, width and height is size of the window in pixels."""
        self.background_colour = background_colour
        
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg=self.background_colour, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self):
        """Tell the window to redraw."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Sets is Running to true."""
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        """Set is Running to False."""
        self.__is_running = False

    def draw_line(self, line: Line, fill_colour:str="black") -> None:
        """Draw a line on the window canvas."""
        line.draw(self.__canvas, fill_colour)