#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     29/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import point
def main():
    pass

def square_all(list):
    array = []
    for i in list:
        array.append(i ** 2)
    return array
def add_n_all(list,n):
    for i in range (len(list)):
        return[i+n for i in list]

def distance_all(list):
    input = []
    for i in list:
        x = i.x
        y = i.y
        input.append (math.sqrt((i.x)**2+(i.y)**2))
    return input








if __name__ == '__main__':
    main()

