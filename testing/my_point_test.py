import unittest

from my_point_class import Point

class testPoint(unittest.TestCase): # inherit from TestCase
    # set up before each test (so each test is independent)
    def setUp(self):
        # before each test, create a fresh Point instance
        self.point = Point(3, 5)
    # declare test cases
    def testPointCounter(self):
        '''how many points will exist?'''
        # self.assertEqual( Point.points, 6) # tests should be independent, but all points exists here
        self.assertGreater(Point.points, 6) # more than one point - one for each test!
    def testMoveByA(self):
        '''test the moveBy method alters x and y correctly'''
        self.point.moveBy(5, 2)
        self.assertEqual( self.point.display(), (8, 7) )
    def testMoveByB(self):
        '''test the moveBy method for ngative values'''
        self.point.moveBy(-5, -2)
        self.assertEqual( self.point.display(), (-2, 3) )
    def testMoveByC(self):
        '''check we can use default or speciofic values for dx and dy'''
        self.point.moveBy(dy=9) # use the default dx
        self.assertEqual( self.point.display(), (3, 14) )
    def testHypot(self):
        self.point.moveBy(0, -1) # we now have (3, 4)
        r = self.point.hypot()
        self.assertEqual( r, 5.00 ) # NB the hypot wll be a float
    def testHypotB(self):
        r = self.point.hypot()
        self.assertAlmostEqual( r, 5.83, places=2 )
    def testExceptionRaised(self):
        with self.assertRaises(TypeError):
            Point('3', 4) # string where we expected an int

if __name__ == '__main__':
    unittest.main() # this will invoke our tests - runs aything beginning with 'test'