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
def letter(row, col):
      if(row==9 and col==9):
        return 'Z'
      else:
        return 'G'

if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
