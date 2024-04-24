from classes.helpers import Vector2
from classes.maze import Maze
from classes.window import Window


def main() -> None:
    win = Window(800, 600)

    top_left_corner = Vector2(10, 10)
    size_of_maze = Vector2(10, 10)
    cell_size = Vector2(50, 50)
    maze = Maze(top_left_corner, size_of_maze, cell_size, win)

    _ = maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
