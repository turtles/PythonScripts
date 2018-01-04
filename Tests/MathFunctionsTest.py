from Math.MathFunctions import clamp, pointAngle, pointDistance
import unittest


class TestPointMethods(unittest.TestCase):
    def test_point(self):
        point1 = (0, 0)
        point2 = (2, 4)

        angle = pointAngle(point1[0], point1[1], point2[0], point2[1])
        dist = pointDistance(point1[0], point1[1], point2[0], point2[1])

        self.assertAlmostEqual(angle, 1.1071487177940904)
        self.assertAlmostEqual(dist, 4.47213595499958)


class TestHelperMethods(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(10, 1, 5), 5)
        self.assertEqual(clamp(0, 1, 5), 1)
        self.assertEqual(clamp(3, 1, 5), 3)
        self.assertEqual(clamp(5, 1, 5), 5)


if __name__ == '__main__':
    unittest.main()
