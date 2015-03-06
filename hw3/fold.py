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
    dex = 0
    array = []
    for i in list:
        s = s + list[dex]
        dex = dex + 1
def index_of_smallest(list):
    if(len(list)>0):
        smallest = list[0]
        for i in list:
            if i < smallest:
                smallest = i
        return smallest
    else:
        return -1
def nearest_origin(list):
    array = []
    x1 = 0
    y1 = 0
    formula = math.hypot(x2 - x1, y2 - y1)
    for i in list:
        x2 = i.x
        y2 = i.y
        dist = formula(index[0])
        if i > dist:
            dist = i
        return distance











