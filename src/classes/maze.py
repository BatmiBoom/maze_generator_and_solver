import random
import time

from classes.cell import Cell
from classes.cell import Walls
from classes.helpers import Vector2
from classes.window import Window


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

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        for r in range(self.size_of_maze.row):
            col_cells = []
            for c in range(self.size_of_maze.col):
                col_cells.append(
                    Cell(self._win)
                )

            self._cells.append(col_cells)

        for r in range(self.size_of_maze.row):
            col_cells = []
            for c in range(self.size_of_maze.col):
                self._draw_cell(r, c)

    def _draw_cell(self, row: int, col: int) -> None:
        row_1 = self.top_left_corner.row + row * self.cell_size.row
        col_1 = self.top_left_corner.col + col * self.cell_size.col
        row_2 = row_1 + self.cell_size.row
        col_2 = col_1 + self.cell_size.col
        left_top_corner = Vector2(row_1, col_1)
        right_bottom_corner = Vector2(row_2, col_2)

        self._cells[row][col].draw("black", left_top_corner, right_bottom_corner)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_walls[Walls.TOP.value] = False
        self._draw_cell(0, 0)

        self._cells[self.size_of_maze.row - 1][self.size_of_maze.col- 1].has_walls[Walls.BOTTOM.value] = False
        self._draw_cell(self.size_of_maze.row - 1, self.size_of_maze.col - 1)

    def _break_walls_r(self, row: int, col: int) -> None:
        self._cells[row][col].visited = True
        while True:
            next_index_list = []

            # TOP
            if row > 0 and not self._cells[row - 1][col].visited:
                next_index_list.append((row - 1, col))

            # RIGHT
            if col + 1 < self.size_of_maze.col and not self._cells[row][col + 1].visited:
                next_index_list.append((row, col + 1))

            # BOTTOM
            if row + 1 < self.size_of_maze.row and not self._cells[row + 1][col].visited:
                next_index_list.append((row + 1, col))

            # LEFT
            if col > 0 and not self._cells[row][col - 1].visited:
                next_index_list.append((row, col - 1))

            if len(next_index_list) == 0:
                self._draw_cell(row, col)
                self._animate()
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # TOP
            if next_index[0] == row - 1:
                self._cells[row][col].has_walls[Walls.TOP.value] = False
                self._cells[row - 1][col].has_walls[Walls.BOTTOM.value] = False

            # RIGHT
            if next_index[1] == col + 1:
                self._cells[row][col].has_walls[Walls.RIGHT.value] = False
                self._cells[row][col + 1].has_walls[Walls.LEFT.value] = False

            # BOTTOM
            if next_index[0] == row + 1:
                self._cells[row][col].has_walls[Walls.BOTTOM.value] = False
                self._cells[row + 1][col].has_walls[Walls.TOP.value] = False

            # LEFT
            if next_index[1] == col - 1:
                self._cells[row][col].has_walls[Walls.LEFT.value] = False
                self._cells[row][col - 1].has_walls[Walls.RIGHT.value] = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self) -> None:
        for cells in self._cells:
            for cell in cells:
                cell.visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, row: int, col: int) -> bool:
        self._animate()
        self._cells[row][col].visited = True

        # END CONDITION
        if row == self.size_of_maze.row - 1 and col == self.size_of_maze.col - 1:
            return True

        # TOP
        if (
            row > 0
            and not self._cells[row][col].has_walls[Walls.TOP.value]
            and not self._cells[row - 1][col].visited
            ):
                self._cells[row][col].draw_move(self._cells[row - 1][col], "red")
                if self._solve_r(row - 1, col):
                    return True
                else:
                    self._cells[row][col].draw_move(self._cells[row - 1][col], "red", True)

        # RIGHT
        if (
            col + 1 < self.size_of_maze.col 
            and not self._cells[row][col].has_walls[Walls.RIGHT.value]
            and not self._cells[row][col + 1].visited
            ):
                self._cells[row][col].draw_move(self._cells[row][col + 1], "yellow")
                if self._solve_r(row, col + 1):
                    return True
                else:
                    self._cells[row][col].draw_move(self._cells[row][col + 1], "yellow", True)


        # BOTTOM
        if (
            row + 1 < self.size_of_maze.row 
            and not self._cells[row][col].has_walls[Walls.BOTTOM.value]
            and not self._cells[row + 1][col].visited
            ):
                self._cells[row][col].draw_move(self._cells[row + 1][col], "green")
                if self._solve_r(row + 1, col):
                    return True
                else:
                    self._cells[row][col].draw_move(self._cells[row + 1][col], "green", True)

        # LEFT
        if (
            col > 0
            and not self._cells[row][col].has_walls[Walls.LEFT.value]
            and not self._cells[row][col - 1].visited
            ):
                self._cells[row][col].draw_move(self._cells[row][col - 1], "black")
                if self._solve_r(row, col - 1):
                    return True
                else:
                    self._cells[row][col].draw_move(self._cells[row][col - 1], "black", True)

        return False

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)
