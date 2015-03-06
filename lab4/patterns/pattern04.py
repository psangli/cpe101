#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     27/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import driver
def main():
    pass
def letter(row,col):
    if(row>1 and row<5 and col>2 and col<7):
        return 'M'
    else:
        return 'S'





if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
