import unittest
from triangle import triangleMath

class TestTriangle(unittest.TestCase):

    def testTriangleArea(self):

        self.assertEqual(12, triangleMath.area(6,4))
        self.assertEqual(0, triangleMath.area(0,0))
        self.assertEqual(24, triangleMath.area(12,4))
        self.assertEqual(6, triangleMath.area(3,4))
        self.assertEqual(100, triangleMath.area(20,10))

    def testFloatNumbers(self):
        self.assertAlmostEqual(17.79875, triangleMath.area(7.25,4.91))

    def testNegsNumbers(self):
        with self.assertRaises(ValueError):
            triangleMath.area(9, -10)

        with self.assertRaises(ValueError):
            triangleMath.area(-9, 10)

        with self.assertRaises(ValueError):
            triangleMath.area(-9, -10)

        with self.assertRaises(ValueError):
            triangleMath.area(9, -10)
