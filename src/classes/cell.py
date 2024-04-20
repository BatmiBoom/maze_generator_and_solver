from enum import Enum
from tkinter import Canvas
from typing import Self

from classes.helpers import Vector2
from classes.line import Line


class Walls(Enum):
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3


class Cell:
    def __init__(
        self,
        left_top_corner: Vector2,
        right_bottom_corner: Vector2,
        canvas: Canvas,
        has_walls: list[bool] = [True, True, True, True],
        visited: bool = False,
    ) -> None:
        self.has_walls = has_walls
        self.left_top_corner = left_top_corner
        self.left_bottom_corner = Vector2(left_top_corner.x, right_bottom_corner.y)
        self.right_top_corner = Vector2(right_bottom_corner.x, left_top_corner.y)
        self.right_bottom_corner = right_bottom_corner
        self.visited = visited
        self.canvas = canvas

    def draw(
        self,
        fill_color: str,
    ) -> None:
        if self.has_walls[Walls.TOP.value]:
            line = Line(self.left_top_corner, self.right_top_corner)
            line.draw(self.canvas, fill_color)
        else:
            line = Line(self.left_top_corner, self.right_top_corner)
            line.draw(self.canvas, "white")

        if self.has_walls[Walls.LEFT.value]:
            line = Line(self.left_top_corner, self.left_bottom_corner)
            line.draw(self.canvas, fill_color)
        else:
            line = Line(self.left_top_corner, self.left_bottom_corner)
            line.draw(self.canvas, "white")

        if self.has_walls[Walls.BOTTOM.value]:
            line = Line(self.left_bottom_corner, self.right_bottom_corner)
            line.draw(self.canvas, fill_color)
        else:
            line = Line(self.left_bottom_corner, self.right_bottom_corner)
            line.draw(self.canvas, "white")

        if self.has_walls[Walls.RIGHT.value]:
            line = Line(self.right_top_corner, self.right_bottom_corner)
            line.draw(self.canvas, fill_color)
        else:
            line = Line(self.right_top_corner, self.right_bottom_corner)
            line.draw(self.canvas, "white")

    def draw_move(self, to_cell: Self, undo=False) -> None:
        fill_color = "red" if not undo else "gray"

        x_mid = (self.left_top_corner.x + self.right_bottom_corner.x) / 2
        y_mid = (self.left_top_corner.y + self.right_bottom_corner.y) / 2

        to_x_mid = (to_cell.left_top_corner.x + to_cell.right_bottom_corner.x) / 2
        to_y_mid = (to_cell.left_top_corner.y + to_cell.right_bottom_corner.y) / 2

        line = Line(Vector2(x_mid, y_mid), Vector2(to_x_mid, to_y_mid))
        line.draw(self.canvas, fill_color)

    def remove_wall(
        self,
        top: bool | None = None,
        left: bool | None = None,
        bottom: bool | None = None,
        right: bool | None = None,
    ) -> None:
        if top is not None:
            self.has_walls[Walls.TOP.value] = top

        if left is not None:
            self.has_walls[Walls.LEFT.value] = left

        if bottom is not None:
            self.has_walls[Walls.BOTTOM.value] = bottom

        if right is not None:
            self.has_walls[Walls.RIGHT.value] = right

