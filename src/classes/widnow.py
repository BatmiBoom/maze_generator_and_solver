from tkinter import Canvas
from tkinter import Tk


class Window:
    def __init__(self, width, height) -> None:
        self.root_widget = Tk("Maze Solver")
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(
            self.root_widget, cnf={"width": width, "height": height, "bg": "white"}
        )
        self.canvas.pack()

        self.running = False

    def redraw(self) -> None:
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

