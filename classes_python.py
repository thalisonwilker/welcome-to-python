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


rect1 = Rectangle(10, 40)
rect2 = Rectangle(40, 10)

print(rect1 == rect2)  # False

# adicionando os valores do primeiro retângulo ao segundo
rect2.width = rect1.width
rect2.height = rect1.height

print(rect1 == 4)  # True
