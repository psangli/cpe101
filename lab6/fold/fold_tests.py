import unittest
import fold
import point

class TestCases(unittest.TestCase):
   def test_sum(self):
    test_list = [1,2,3]
    self.assertEqual(fold.sum(test_list),6)
   def test_index(self):
    test_list = []
    self.assertAlmostEqual(fold.index_of_smallest(test_list),-1)
   def test_distance(self):
    point1 = point.Point(1,1)
    point2 = point.Point(7,12)
    test_list = [point1,point2]
    self.assertAlmostEqual(fold.nearest_origin(test_list),(0))

      # Add code here.


    pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

