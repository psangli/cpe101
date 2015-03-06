import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_case(self):
      # Add code here.
      x = 2
      y = 1
      self.assertAlmostEqual(conditional.max_101(x,y), 2)


   def test_case3(self):
    x1 = 5
    x2 = 6
    y1 = 6
    y2 = 7
    z1 = 7
    z2 = 8
    self.assertTrue(conditional.max_of_three(x1,y1,z1), 7)
    self.assertTrue(conditional.max_of_three(x2,y2,z2), 8)




   def test_rental (self):
        day1=6
        day2=10
        day3=17
        day4=999
        self.assertTrue(conditional.rental_late_fee(day1),5)
        self.assertTrue(conditional.rental_late_fee(day2),7)
        self.assertTrue(conditional.rental_late_fee(day3),19)
        self.assertTrue(conditional.rental_late_fee(day4),100)

pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

