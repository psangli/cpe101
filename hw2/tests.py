#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Psangli
#
# Created:     19/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import math
import data
import vector_math
import utility
class TestData(unittest.TestCase):
   def test_point_1(self):
    test_point_1 = data.Point(1.0, 2.0, 3.0)
    self.assertAlmostEqual (test_point_1.x, 1.0)
    self.assertAlmostEqual (test_point_1.y, 2.0)
    self.assertAlmostEqual (test_point_1.z, 3.0)
   def test_point_2(self):
    test_point_2 = data.Point(4.0, 5.0, 6.0)
    self.assertAlmostEqual (test_point_2.x, 4.0)
    self.assertAlmostEqual (test_point_2.y, 5.0)
    self.assertAlmostEqual (test_point_2.z, 6.0)

   def test_equality_point_1(self):
     p1 = data.Point(1.0,2.0,3.0)
     p2 = data.Point(1.0,2.0,3.0)
     test = p1.__eq__(p2)
     self.assertTrue(test)
     pass
   def test_equality_point_2(self):
     p1 = data.Point(4.0,5.0,6.0)
     p2 = data.Point(4.0,5.0,6.0)
     test = p1.__eq__(p2)
     self.assertTrue(test)


   def test_vector_1(self):
    test_vector_1 = data.Vector(1.0, 2.0, 3.0)
    self.assertAlmostEqual (test_vector_1.x, 1.0)
    self.assertAlmostEqual (test_vector_1.y, 2.0)
    self.assertAlmostEqual (test_vector_1.z, 3.0)
   def test_vector_2(self):
    test_vector_2 = data.Vector(4.0, 5.0, 6.0)
    self.assertAlmostEqual (test_vector_2.x, 4.0)
    self.assertAlmostEqual (test_vector_2.y, 5.0)
    self.assertAlmostEqual (test_vector_2.z, 6.0)

   def test_equality_vector1(self):
    v1 = data.Vector(1.0,2.0,3.0)
    v2 = data.Vector(1.0,2.0,3.0)
    test = v1.__eq__(v2)
    self.assertTrue(test)
    pass
   def test_equality_vector2(self):
    v1 = data.Vector(4.0,5.0,6.0)
    v2 = data.Vector(4.0,5.0,6.0)
    test = v1.__eq__(v2)
    self.assertTrue(test)
    pass


   def test_ray_1(self):
    test_ray_1 = data.Ray (data.Point(1.0,2.0,3.0), data.Vector(1.0,2.0,3.0))
    self.assertAlmostEqual (test_ray_1.pt.x, 1.0)
    self.assertAlmostEqual (test_ray_1.pt.y, 2.0)
    self.assertAlmostEqual (test_ray_1.pt.z, 3.0)
    self.assertAlmostEqual (test_ray_1.dir.x, 1.0)
    self.assertAlmostEqual (test_ray_1.dir.y, 2.0)
    self.assertAlmostEqual (test_ray_1.dir.z, 3.0)
   def test_ray_2(self):
    test_ray_2 = data.Ray (data.Point(2.0,3.0,4.0), data.Vector(5.0,6.0,7.0))
    self.assertAlmostEqual (test_ray_2.pt.x, 2.0)
    self.assertAlmostEqual (test_ray_2.pt.y, 3.0)
    self.assertAlmostEqual (test_ray_2.pt.z, 4.0)
    self.assertAlmostEqual (test_ray_2.dir.x, 5.0)
    self.assertAlmostEqual (test_ray_2.dir.y, 6.0)
    self.assertAlmostEqual (test_ray_2.dir.z, 7.0)


   def test_equality_ray1(self):
    p1 = data.Point(4,5,6)
    v1 = data.Vector(1,2,3)
    p2 = data.Point(4,5,6)
    v2 = data.Vector(1,2,3)
    r1 = data.Ray(p1, v1)
    r2 = data.Ray(p2, v2)
    test = r1.__eq__(r2)
    self.assertTrue(test)
    pass
   def test_equality_ray2(self):
    p1 = data.Point(4,5,6)
    v1 = data.Vector(1,2,3)
    p2 = data.Point(4,5,6)
    v2 = data.Vector(1,2,3)
    r1 = data.Ray(p1, v1)
    r2 = data.Ray(p2, v2)
    test = r1.__eq__(r2)
    self.assertTrue(test)
    pass


   def test_sphere_1(self):
    test_sphere_1 = data.Sphere (data.Point(1.0,2.0,3.0), 1.0)
    self.assertAlmostEqual (test_sphere_1.center.x, 1.0)
    self.assertAlmostEqual (test_sphere_1.center.y, 2.0)
    self.assertAlmostEqual (test_sphere_1.center.z, 3.0)
    self.assertAlmostEqual (test_sphere_1.radius, 1.0)

   def test_sphere_2(self):
    test_sphere_2 = data.Sphere (data.Point(2.0,3.0,4.0), 5.0)
    self.assertAlmostEqual (test_sphere_2.center.x, 2.0)
    self.assertAlmostEqual (test_sphere_2.center.y, 3.0)
    self.assertAlmostEqual (test_sphere_2.center.z, 4.0)
    self.assertAlmostEqual (test_sphere_2.radius, 5.0)

   def test_equality_sphere_one(self):
      s1 = data.Sphere(data.Point(1,2,3), 4.0)
      s2 = data.Sphere(data.Point(1,2,3), 4.0)
      test = s1.__eq__(s2)
      self.assertTrue(test)
      pass
   def test_equality_sphere_two(self):
      s1 = data.Sphere(data.Point(5,6,7), 8.0)
      s2 = data.Sphere(data.Point(5,6,7), 8.0)
      test = s1.__eq__(s2)
      self.assertTrue(test)
      pass

   def test_scale_vector(self):
    test_scale = (vector_math.Vector(1.0,2.0,3.0))
    scalar_1 = 2.0
    self.assertAlmostEqual (vector_math.scale_vector (test_scale, scalar_1),(2.0,4.0,6.0))

   def test_dot_vector(self):
    test_dot = vector_math.Vector(1.0,2.0,3.0)
    test_dot2 = vector_math.Vector(4.0,5.0,6.0)
    test_dot3 = vector_math.dot_vector(test_dot,test_dot2)
    self.assertTrue(test_dot3==32.0)

   def test_length(self):

    test_length2 = vector_math.length_vector(vector_math.Vector(1.0,2.0,3.0))
    self.assertTrue (test_length2 == math.sqrt(14.0))


   def test_normalize(self):
    v1 = vector_math.Vector(1.0,2.0,3.0)
    length = vector_math.length_vector(v1)
    self.assertTrue( vector_math.normalize_vector(v1),vector_math.Vector(1.0/length,2.0/length,3.0/length))


   def test_difference_point(self):
    p1 = vector_math.Point(4.0,5.0,6.0)
    p2 = vector_math.Point(1.0,2.0,3.0)
    p3 = vector_math.difference_point(p1,p2)
    self.assertTrue(p3 == (3.0,3.0,3.0))

   def test_difference_vector(self):
    v1 = vector_math.Vector(4.0,5.0,6.0)
    v2 = vector_math.Vector(1.0,2.0,3.0)
    v3 = vector_math.difference_vector(v1,v2)
    self.assertTrue(v3 == (3.0,3.0,3.0))

   def test_translate_point(self):
    p1 = vector_math.Point(9.0, 0.0, 1.0)
    v1 = vector_math.Vector(1.0,2.0,3.0)
    r = vector_math.translate_point(p1,v1)
    self.assertTrue(r == (10.0,2.0,4.0))

   def test_vector_from_to(self):
    fp = vector_math.Point(1.0,2.0,3.0)
    tp = vector_math.Point(4.0,5.0,6.0)
    d = vector_math.difference_point(tp,fp)
    self.assertTrue(d == (3.0,3.0,3.0))













if __name__ == '__main__':
   unittest.main()


