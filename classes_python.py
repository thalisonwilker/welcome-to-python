class Rectangle(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._height + self._width)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __repr__(self):
        return f'Rectangle with width={self._width} and height={self._height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width == other.width) and (self._height == other.height)
        else:
            raise ArithmeticError(f'{type(other)} is not a Rectangle class instance')

    def __add__(self, other):
        width = self._width + other.width
        height = self._height + other.height
        return Rectangle(width=width, height=height)

    def __sub__(self, other):
        width = self._width - other.width
        height = self._height - other.height
        return Rectangle(width=width, height=height)

    def __mul__(self, other):
        width = self._width * other.width
        height = self._height * other.height
        return Rectangle(width=width, height=height)

    def __truediv__(self, other):
        width = self._width / other.width
        height = self._height / other.height
        return Rectangle(width=width, height=height)

    def __lt__(self, other):
        return self.area() < other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 4)

print(rect2 < rect1)