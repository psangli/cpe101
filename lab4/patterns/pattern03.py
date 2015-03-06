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
    if(col<=9):
        return 'X'
    else:
        return 'O'

if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
