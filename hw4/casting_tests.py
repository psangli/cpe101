#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     14/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cast
from data import *
#from vector_math import *

width = 1024
height = 768
print ('P3')
print(str(width))
print(str(height))
print('255')



eye_point = Point(0.0,0.0,-14.0)
light = Light(Point(-100,100,-100), Color(1.5,1.5,1.5))
spherelist = [Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1),Finish(0.2,.4,.5,.05)), Sphere(Point(0.5,1.5,-3.0), 0.5,Color(1,0,0),Finish(0.4,.4,.5,.05))]
cast.cast_all_rays(-10,10,-7.5,7.5,width,height,eye_point,spherelist,Color(1,1,1),light)
