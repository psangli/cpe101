import unittest
import convert

class TestConvert(unittest.TestCase):
   def test_convert(self):
      self.assertTrue(convert.float_default('5',-1.0),5.0)
   def test_convert2(self):
      self.assertTrue(convert.float_default('chris',-1.0),-1.0)
      pass


if __name__ == '__main__':
   unittest.main()

