class Vector2:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def sum(self, point_2):
        return Vector2(self.x + point_2.x, self.y + point_2.y)

    def distance(self, point_2):
        return Vector2(self.x - point_2.x, self.y - point_2.y)

