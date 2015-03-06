#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     28/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import driver
def main():
    pass
def letter(row,col):
    if(col==row):
        return 'X'
    if(col + 1==7 - row):
        return 'X'
    else:
        return 'O'

if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
