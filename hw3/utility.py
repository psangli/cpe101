#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Psangli
#
# Created:     26/01/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)