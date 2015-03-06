import unittest
import string_101

class TestString(unittest.TestCase):
   def test_lower(self):
      str = "abc"
      self.assertEqual(string_101.str_rot_13(str),"nop")

   def test_str_translate(self):
      self.assertEqual(string_101.str_translate_101('abcdcba','a','x'),'xbcdcbx')

if __name__ == '__main__':
   unittest.main()

