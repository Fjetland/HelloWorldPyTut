class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def print(self):
        print(f"({self.x}, {self.y})")


point = Point(10, 2)
point.x = 11
print(point.x)
point.print()


