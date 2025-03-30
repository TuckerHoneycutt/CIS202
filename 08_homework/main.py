class Shape:
    def area(self):
        raise NotImplementedError("Subclass must be implement area() method")

    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.area()}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

square = Square(5)
triangle = Triangle(6,4)

print(square)
print(triangle)
