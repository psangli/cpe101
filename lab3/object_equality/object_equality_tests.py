import unittest
import point
import utility

class TestCases(unittest.TestCase):
   def test_point_one(self):
      pt = point.Point(1, 2)
      self.assertAlmostEqual(pt.x, 1)
      self.assertAlmostEqual(pt.y, 2)


   def test_point_two(self):
      pt = point.Point(-4.7, 19.2)
      self.assertAlmostEqual(pt.x, -4.7)
      self.assertAlmostEqual(pt.y, 19.2)


   def test_equality(self):
      equality_1 = utility.epsilon_equal(1.00000001,1.000001)
      self.assertTrue(equality_1)
      pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

