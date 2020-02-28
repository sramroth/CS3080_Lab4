from Shape import *
class Triangle(Shape):
    def __init__(self, base):
        super().__init__()
        self.base = base

    def draw(self):
        super().draw()
        print("Triangle Draw")
        for i in range(1, self.base + 1):
            print("*" * i)