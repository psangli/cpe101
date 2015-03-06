#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     04/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def groups_of_3(list):
   array = []
   newArray = []
   g = 3
   for i in range(0, len(list),g):
    array = list[i:i+g]
    newArray.append(array)
   return newArray




if __name__ == '__main__':
    main()

