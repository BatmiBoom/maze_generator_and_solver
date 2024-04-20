from tkinter import Canvas

from classes.helpers import Vector2


class Line:
    def __init__(self, point_1: Vector2, point_2: Vector2, width: int = 2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
        self.width = width

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=self.width,
        )
        canvas.pack()

