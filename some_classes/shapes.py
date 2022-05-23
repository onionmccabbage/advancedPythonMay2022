from c import Shape


class Square(Shape):
    def __init__(self, name, sides):
        super().__init__(name, sides)


class Hexagon(Shape):
    def __init__(self, name, sides, arbitrary):
        super().__init__(name, sides)
        self.__arbitrary = arbitrary # double-underscore 'mangles' the name so it is hard to access
    @property
    def arbitrary(self):
        return self.__arbitrary # we CAN access mangled members from within the class
    @arbitrary.setter
    def arbitrary(self, a):
        self.__arbitrary = a # we would validate before setting!

if __name__ == '__main__': # we call these 'dunder' for double-underscore
    s = Square('Square', 4)
    h = Hexagon('Hexagon', 6, {'use':'bees'})
    print(s)
    print(h)
    # h.arbitrary = False
    print(h.arbitrary) # we CANNOT directly access the mangled property - we must use the getter method