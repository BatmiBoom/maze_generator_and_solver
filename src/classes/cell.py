from enum import Enum
from typing import Self

from classes.helpers import Vector2
from classes.line import Line
from classes.window import Window


class Walls(Enum):
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3


class Cell:
    def __init__(
        self,
        win = None
    ) -> None:
        self.has_walls = [True, True, True, True]
        self.visited = False
        self.left_top_corner = None
        self.left_bottom_corner = None
        self.right_top_corner = None 
        self.right_bottom_corner = None
        self._win: Window | None = win

    def draw(
        self,
        fill_color: str,
        left_top_corner: Vector2,
        right_bottom_corner: Vector2,
    ) -> None:
        if self._win is None:
            return

        self.left_top_corner = left_top_corner
        self.left_bottom_corner = Vector2(right_bottom_corner.row, left_top_corner.col)
        self.right_top_corner = Vector2(left_top_corner.row, right_bottom_corner.col)
        self.right_bottom_corner = right_bottom_corner

        if self.has_walls[Walls.TOP.value]:
            line = Line(self.left_top_corner, self.right_top_corner)
            self._win.draw_line(line, fill_color)
        else:
            line = Line(self.left_top_corner, self.right_top_corner)
            self._win.draw_line(line, "white")

        if self.has_walls[Walls.LEFT.value]:
            line = Line(self.left_top_corner, self.left_bottom_corner)
            self._win.draw_line(line, fill_color)
        else:
            line = Line(self.left_top_corner, self.left_bottom_corner)
            self._win.draw_line(line, "white")

        if self.has_walls[Walls.BOTTOM.value]:
            line = Line(self.left_bottom_corner, self.right_bottom_corner)
            self._win.draw_line(line, fill_color)
        else:
            line = Line(self.left_bottom_corner, self.right_bottom_corner)
            self._win.draw_line(line, "white")

        if self.has_walls[Walls.RIGHT.value]:
            line = Line(self.right_top_corner, self.right_bottom_corner)
            self._win.draw_line(line, fill_color)
        else:
            line = Line(self.right_top_corner, self.right_bottom_corner)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: Self, fill_color: str, undo=False) -> None:

        if self._win is None:
            print("No Win")
            return

        if self.left_top_corner is None or self.right_bottom_corner is None:
            print("No TOP CORNER")
            return

        if to_cell.left_top_corner is None or to_cell.right_bottom_corner is None:
            print("No BOTTOM CORNER")
            return

        row_mid = (self.left_top_corner.row + self.right_bottom_corner.row) // 2
        col_mid = (self.left_top_corner.col + self.right_bottom_corner.col) // 2

        to_row_mid = (to_cell.left_top_corner.row + to_cell.right_bottom_corner.row) // 2
        to_col_mid = (to_cell.left_top_corner.col + to_cell.right_bottom_corner.col) // 2

        if undo: 
            fill_color = "gray"

        line = Line(Vector2(row_mid, col_mid), Vector2(to_row_mid, to_col_mid))
        self._win.draw_line(line, fill_color)

    def __str__(self):
        return f"LBC {self.left_bottom_corner} LTC {self.left_top_corner} RBC {self.right_bottom_corner} RTC {self.right_top_corner} HW {self.has_walls}"
