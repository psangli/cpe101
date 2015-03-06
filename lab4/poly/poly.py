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

def main():
    pass
def poly_add2(poly1,poly2):
    output = []
    output.append(poly1[0] + poly2[0])
    output.append(poly1[1] + poly2[1])
    output.append(poly1[2] + poly2[2])
    return output

def poly_mult2(poly1,poly2):
	output = []
	output.append(poly1[0]*poly2[0])
	output.append(poly1[1]+poly2[1])
	output.append([])
	output.append([])
	output.append(poly1[2]*poly2[2])
	return output
if __name__ == '__main__':
    main()
