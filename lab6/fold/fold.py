#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     03/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import point
import math
import vector_math
def main():
    pass

if __name__ == '__main__':
    main()

def sum(list):
    s = 0
    for i in list:
        s = s + i
    return s




def index_of_smallest(list):
    if(len(list) == 0):
        return -1
    else:
        smallest = list[0]
        for list[i] in list:
            if i < smallest:
                smallest = list[i]
        return smallest

def distance(i):
    x=i.x
    y=i.y
    dist = math.sqrt(x**2 + y**2)
    return dist
def nearest_origin(list):
    if(len(list) == 0):
        return -1
    else:
        smallest = distance(list[0])
        dex = 0
        realDex = 0
        for i in list:

            if distance(i) < smallest:
                smallest = list(realDex)
                dex = realDex
            realDex =realDex +1
        return dex







