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
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def __eq__(self, other ):
       return((self.center,other.center) and (self.radius,other.radius))

if __name__ == '__main__':
    main()
