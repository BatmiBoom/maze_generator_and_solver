class Vector2:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def sum(self, point_2):
        return Vector2(self.row + point_2.row, self.col + point_2.col)

    def distance(self, point_2):
        return Vector2(self.row - point_2.row, self.col - point_2.col)

    def __str__(self):
        return f"Row = {self.row}, Col= {self.col}"
