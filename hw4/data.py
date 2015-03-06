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
        return ((self.pt,other.pt) and (self.dir, other.dir))
class Sphere(object):
    def __init__(self, center, radius, color,finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish
    def __eq__(self, other ):
       return((self.center,other.center) and (self.radius,other.radius))
class Color(object):
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
class Finish(object):
    def __init__(self,ambient,diffuse,specular,roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self,other):
        return (epsilon_equal(self.ambient,other.ambient) and epsilon_equal(self.diffuse,other.diffuse) and epsilon_equal(self.roughness,other.roughness))
class Light(object):
    def __init__(self,pt,color):
        self.pt = pt
        self.color = color
    def __eq__(self,other):
        return (epsilon_equal(self.pt,other.pt) and epsilon_equal(self.color,other.color))
if __name__ == '__main__':
    main()
