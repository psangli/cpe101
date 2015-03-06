#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     22/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
def max_101(x,y):
    if (x>y):
     return x
    else:
     return y
def max_of_three(x,y,z):
    if (x>y):
        if(x>z):
            return x
    if(y>z):
        if(y>x):
            return y
    if(z>x):
        if(z>y):
            return z

def rental_late_fee(x):
    if (x<=0):
        return 0
    if (x<=9):
        return 5
    if (x<=15):
        return 7
    if (x<=24):
        return 19
    if (x>24):
        return 100



if __name__ == '__main__':
    main()
