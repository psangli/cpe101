import unittest
import filter
import point

class TestCases(unittest.TestCase):
    def test_are_positive_1(self):
        l1 = [1,2,-3]
        output = filter.are_postitive (l1)
        self.assertEqual(output, [1,2])
    def test_are_positive_2(self):
        l1 = [2,3,-4]
        is_positive = filter.are_postitive(l1)
        self.assertEqual(is_positive, [2,3])

    def test_are_greater_than1(self):
        l1 = [2,3,4]
        n = 3
        test_greater = filter.are_greater_than(l1,3)
    def test_are_greater_than2(self):
        l1 = [5,6,7]
        n = 6
        test_greater = filter.are_greater_than(l1,6)
    def test_are_in_first_quad1(self):
        l1 = [point.Point(1.0,2.0)]
        out =filter.are_in_first_quadrant(l1)
        self.assertTrue (out[0].__eq__( point.Point(1.0,2.0)))
    def test_are_in_first_quad1(self):
        l1 = [point.Point(3.0,4.0)]
        out =filter.are_in_first_quadrant(l1)
        self.assertTrue (out[0].__eq__( point.Point(3.0,4.0)))



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

