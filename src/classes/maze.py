import random
import time

from classes.cell import Cell
from classes.helpers import Vector2
from classes.widnow import Window


class Maze:
    def __init__(
        self,
        top_left_corner: Vector2,
        size_of_maze: Vector2,
        cell_size: Vector2,
        win: Window,
        seed: int | None = None,
    ) -> None:
        self.top_left_corner = top_left_corner
        self.size_of_maze = size_of_maze
        self.cell_size = cell_size
        self._win = win
        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        if seed:
            random.seed(seed)

    def _create_cells(self) -> None:
        for r in range(self.size_of_maze.x):
            col_cells = []
            for c in range(self.size_of_maze.y):
                x1 = self.top_left_corner.x + r * self.cell_size.x
                y1 = self.top_left_corner.y + c * self.cell_size.y
                x2 = x1 + self.cell_size.x
                y2 = y1 + self.cell_size.y
                left_top_corner = Vector2(x1, y1)
                righ_bottom_corner = Vector2(x2, y2)
                col_cells.append(
                    Cell(left_top_corner, righ_bottom_corner, self._win.canvas)
                )

            self._cells.append(col_cells)

        self._draw_cells()

    def _draw_cells(self) -> None:
        for cells in self._cells:
            for cell in cells:
                cell.draw("black")
                self._animate()

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.remove_wall(top=False)
        entrance_cell.draw("black")
        self._animate()

        exit_cell = self._cells[int(self.size_of_maze.x) - 1][
            int(self.size_of_maze.y) - 1
        ]
        exit_cell.remove_wall(bottom=False)
        exit_cell.draw("black")
        self._animate()

    def _break_walls_r(self, row: int, col: int) -> None:

        while True:
            self._cells[row][col].visited = True  # (0, 0)
            next_index_list = []

            # TOP
            if row > 0 and not self._cells[row - 1][col].visited:
                next_index_list.append((row - 1, col))

            # RIGHT
            if col + 1 < self.size_of_maze.x and not self._cells[row][col + 1].visited:
                next_index_list.append((row, col + 1))

            # BOTTOM
            if row + 1 < self.size_of_maze.y and not self._cells[row + 1][col].visited:
                next_index_list.append((row + 1, col))

            # LEFT
            if col > 0 and not self._cells[row][col - 1].visited:
                next_index_list.append((row, col - 1))

            # next_index_list = [(0, 1), (1, 0)]

            if len(next_index_list) == 0:
                self._cells[row][col].draw("black")
                self._animate()
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]  # (0, 1)

            # TOP
            if next_index[1] == row - 1:
                self._cells[row][col].remove_wall(top=False)
                self._cells[row - 1][col].remove_wall(bottom=False)

            # RIGHT
            if next_index[0] == col + 1:
                self._cells[row][col].remove_wall(right=False)
                self._cells[row][col + 1].remove_wall(left=False)

            # BOTTOM
            if next_index[1] == row + 1:
                self._cells[row][col].remove_wall(bottom=False)
                self._cells[row + 1][col].remove_wall(top=False)

            # LEFT
            if next_index[0] == col - 1:
                self._cells[row][col].remove_wall(left=False)
                self._cells[row][col - 1].remove_wall(right=False)

            row = next_index[0]
            col = next_index[1]

    def _reset_cells_visited(self) -> None:
        for cells in self._cells:
            for cell in cells:
                cell.visited = False

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

