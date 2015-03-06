#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     26/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
def main():
    fileInput()
    pass
def fileInput():

    array = sys.argv
    try:
        f = open(array[1], 'r')
        myList = []
        for line in f:
            myList = line.split(" ")
            try:
                print (float(myList[0])  + float(myList[1]))

            except:
                print("cannot add")
        f.close()
    except:
        print("error cannot open file")
        exit









if __name__ == '__main__':
    main()
