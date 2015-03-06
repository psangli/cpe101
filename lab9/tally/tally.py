#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     05/03/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
def main():
    tally()
    pass
def tally():
    if (len(sys.argv) >= 3):
        filename = sys.argv[1]
        col = int(sys.argv[2])
    else:
        print("wrong number of args")
        return
    try:
        input = open(filename, "r")
        sum = 0
        counter = 0
        for line in input:
            counter += 1
            list = line.split()
            if (len(list) > col):
                number = list[col]
                try:
                     fnumber = float(number)
                     sum += fnumber
                except:
                    print ("this is not a number " + counter)
            else:
                print ("no value at col " + counter )
        print (sum)
        return sum
    except:
        print ("file not found")
        return


if __name__ == '__main__':
    main()
