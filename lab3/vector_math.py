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

def main():
    pass

if __name__ == '__main__':
    main()

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
class Vector(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
class Ray(object):
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir
class Sphere(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius



if __name__ == '__main__':
    main()
