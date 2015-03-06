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
def letter(row, col):
	if (row <2) or (row>6):
		return 'T'
	else:
		if(col<4)or(col>12):
			return 'T'
		if(row == 2) or (row==3):
			if (col>9):
				return 'T'
		if(row==4) or (row==5):
			if(col>6)and(col<10):
				return 'X'
			if(col>9)and(col<13):
				return 'B'
		if(row==6):
			if col<7:
				return 'T'
			if(col>6)and(col<13):
				return 'B'
		return 'Z'

if __name__ == '__main__':
    driver.comparePatterns(letter)
    main()
