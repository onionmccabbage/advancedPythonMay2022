# here are some concrete classes



from a import AbsctractShape


class Shape(AbsctractShape):
    def __init__(self, name, sides):
        self.shape_name = name
        self.sides = sides # we COULD write get/set methods for sides
    @property
    def shape_name(self):
        return self.__shape_name
    @shape_name.setter
    def shape_name(self, new_name):
        self.__shape_name = new_name
    def __str__(self):
        return 'This shape is called {} and has {} sides'.format(self.shape_name, self.sides)