#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     19/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
from utility import *
import utility


def main():
    pass

if __name__ == '__main__':
    main()
class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other ):
        return (utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z))

class Vector(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other ):
        return (utility.epsilon_equal(self.x,other.x) and utility.epsilon_equal(self.y,other.y) and utility.epsilon_equal(self.z,other.z))
class Ray(object):
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir
    def __eq__(self, other ):
        return(utility.epsilon_equal(self.pt,other.pt) and utility.epsilon_equal(self.dir, other.dir))
class Sphere(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def __eq__(self, other ):
       return(utility.epsilon_equal(self.center,other.center) and utility.epsilon_equal(self.radius,other.radius))

def scale_vector(vector,scalar):
    return Vector(vector.x*scalar,vector.y*scalar,vector.z*scalar)
def dot_vector(Vector1,Vector2):
    return (Vector1.x * Vector2.x + Vector1.y * Vector2.y + Vector1.z * Vector2.z)
def length_vector(vector):
    return math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
def normalize_vector(v):
    return Vector(v.x/(length_vector(v)),v.y/(length_vector(v)),v.z/(length_vector(v)))
def difference_point(p1, p2):
    return Point(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)
def difference_vector(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
def translate_point(p1, v1):
    return Point(p1.x + v1.x, p1.y + v1.y, p1.z + v1.z)
def vector_from_to(fp,tp):
    return difference_point(tp,fp)

if __name__ == '__main__':
    main()
