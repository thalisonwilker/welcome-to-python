class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle with width={self.width} and height={self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height)
        else:
            raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width=width, height=height)

    def __sub__(self, other):
        width = self.width - other.width
        height = self.height - other.height
        return Rectangle(width=width, height=height)

    def __mul__(self, other):
        width = self.width * other.width
        height = self.height * other.height
        return Rectangle(width=width, height=height)

    def __truediv__(self, other):
        width = self.width / other.width
        height = self.height / other.height
        return Rectangle(width=width, height=height)


rect1 = Rectangle(10, 40)
rect2 = Rectangle(40, 10)

print(rect1 + rect2) # Adição
print(rect1 - rect2) # Subtração
print(rect1 * rect2) # Multiplicação
print(rect1 / rect2) # Divisão
