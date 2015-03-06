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
    if(row<=9):
        return 'R'
    else:
        return 'Q'
if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
