import unittest
import logic

class TestCases(unittest.TestCase):
   def test_case(self):
      # Add code here.

      self.assertTrue(logic.is_even (2),True)
      self.assertTrue(logic.is_even (4),True)
      self.assertTrue(logic.in_an_interval(3),True)
      self.assertTrue(logic.in_an_interval(48),True)


   pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

