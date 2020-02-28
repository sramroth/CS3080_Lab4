from Shape import *
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width

    def draw(self):
        super().draw()
        print("Rectangle Draw")
        for i in range(0, self.height):
            print("*" * self.width)