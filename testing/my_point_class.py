class Point(object):
    '''
    Class representing x-y values of a point in 2-d space
    derive the hypotenuse from x and y values
    '''
    points = 0 # count how many points have ben created
    def __init__(self, x, y):
        self.x = x # this will call the setter method for x
        self.y = y
        Point.points+=1 # every time a new point is created increase the counter
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==int:
            self.__y = new_y
        else:
            raise TypeError
    def hypot(self):
        '''derive the hypotenuse from x and y'''
        h = (self.x**2 + self.y**2)**0.5
        return h
    def display(self):
        return (self.x, self.y) # return a tuple
    def moveBy(self, dx=0, dy=0):
        ''' move the point by dx and dy'''
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    p1 = Point(3,4)
    print( p1.display() )
    print( p1.hypot() ) # 5
    p2 = Point(-3, -4)
    p2.moveBy(6, 7)
    print( p2.display() ) # (3, 3)
    print( Point.points )