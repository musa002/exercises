class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def __str__(self):
        """String representation of the rectangle."""
        return f"Rectangle: width {self.width}, height {self.height}"

rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())
