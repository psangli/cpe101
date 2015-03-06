import unittest
import poly

class TestPoly(unittest.TestCase):
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
       		self.assertAlmostEqual(el1, el2)
    def test_add_poly(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
    def test_mult_poly2(self):
        poly1 = [2.0, 3.0, 2.0]
        poly2 = [4.0, 4.0, 3.0]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [8.0, 7.0,[],[], 6.0])



if __name__ == '__main__':
   unittest.main()