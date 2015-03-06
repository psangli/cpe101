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
    if(col>=row):
        return 'W'
    else:
        return 'T'

if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
