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

def main():
    pass

def are_postitive(list):
    for i in range (len(list)):
        return[i for i in list if i>=0]

def are_greater_than(list,n):
    for i in range (len(list)):
        return[i for i in list if i>n]
   # input = []
    #for i in list:
     #   if i>n:
      #      input.append(i)
        return input
def are_in_first_quadrant(list):
    input = []
    for i in list:
        x = i.x
        y = i.y
        if (x>0 and y>0):
            input.append(i)
    return input

if __name__ == '__main__':
    main()
