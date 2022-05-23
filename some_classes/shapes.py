from c import Shape


class Square(Shape):
    def __init__(self, name, sides):
        super().__init__(name, sides)


class Hexagon(Shape):
    def __init__(self, name, sides):
        super().__init__(name, sides)

if __name__ == '__main__':
    s = Square('Square', 4)
    h = Hexagon('Hexagon', 6)
    print(s)
    print(h)