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
import collisions
from data import *
import vector_math
from utility import *
import cast


class TestData(unittest.TestCase):



   def test_single_ray_cast1(self):
      ray = Ray(Point(1,2,3),Vector(1,2,3))
      sphere1 = Sphere(Point(0,0,0),50,Color(1,0,0),Finish(1,1,1,1))
      sphere2 = Sphere(Point(1,2,0),50,Color(0,1,0),Finish(1,1,1,1))
      sphere3 = Sphere(Point(10,20,0),50,Color(0,0,1),Finish(1,1,1,1))

      self.assertTrue(cast.cast_ray(ray,[sphere1,sphere2,sphere3],Color(1,1,1), Light(Point(1,1,1),Color(1,1,1)),Point(0,0,0)).r == Color(1,0,0).r)


if __name__ == "__main__":
   unittest.main()







if __name__ == "__main__":
   unittest.main()



