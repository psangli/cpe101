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
from data import *
from vector_math import *
from math import *
from utility import *


def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir,ray.dir)
   B = dot_vector(scale_vector(difference_point(ray.pt,sphere.center),2), ray.dir)
   C = dot_vector(difference_point(ray.pt,sphere.center),difference_point(ray.pt,sphere.center)) - (sphere.radius **2)
   if B**2 - (4*A*C) < 0:
      return None
   u = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
   u2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
   if u < 0 and u2 < 0:
      return None

   elif u < 0 and u2 > 0:
      return translate_point(scale_vector(ray.dir, u2),ray.pt)

   elif u > 0 and u2 < 0:
      return translate_point(scale_vector(ray.dir, u),ray.pt)


   else:
      return translate_point(scale_vector(ray.dir, min(u,u2)),ray.pt)



def find_intersection_points(sphere_list,ray):
   list = []
   for i in sphere_list:
      a = sphere_intersection_point(ray, i)
      list.append((i,a))
   return list


def sphere_normal_at_point(sphere,point):
   return normalize_vector(vector_from_to(sphere.center,point))
