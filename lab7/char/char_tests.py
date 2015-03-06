import unittest
import char

class TestChar(unittest.TestCase):
   def test_lower(self):
      c = 'b'
      self.assertEqual(char.is_lower_101(c),True)

   def test_lower2(self):
      c = 'A'
      self.assertEqual(char.is_lower_101(c),False)
   def test_rot_13(self):
    self.assertEqual(char.rot_13('a'),'n')




if __name__ == '__main__':
   unittest.main()

