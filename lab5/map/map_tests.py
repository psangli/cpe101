import unittest
import map
import point

class TestCases(unittest.TestCase):
    def square_all_1(self):
      # Add code here.
        l1 = [1,2,3,4]
        l2 = [1,4,9,16]
        square_all = map.square_all(l1)
        self.assertTrue(square_all == l2)
    def square_all2(self):
        l1 = [5,6,7,8]
        l2 = [25,36,49,64]
        square_all = map.square_all(l1)
        self.assertTrue(square_all == l2)
    def test_add_n_all_1(self):
        l1 = [1,2,3,4]
        n= 2
        add_n_all_1 = map.add_n_all(l1,n)
        self.assertTrue(add_n_all_1 == [3,4,5,6] )
    def test_add_n_all_2(self):
        l1 = [5,6,7,8]
        n= 2
        add_n_all_1 = map.add_n_all(l1,n)
        self.assertTrue(add_n_all_1 == [7,8,9,10] )
    def test_distance_all(self):
        distance = [point.Point(3,4),point.Point(0,0)]
        distance = map.distance_all (distance)
        self.assertTrue(distance, [5.0,0.0])
    def test_distance_all_2(self):
        distance = [point.Point(0,0)]
        distance = map.distance_all (distance)
        self.assertEqual(distance, [0.0])





pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

