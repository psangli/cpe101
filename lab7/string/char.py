#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Psangli
#
# Created:     20/02/2015
# Copyright:   (c) Psangli 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def is_lower_101(ch):
    lower = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in lower:
        if (ch == i):
            return True
    else:
        return False
def rot_13(ch):
    letters = list('abcdefghijklmnopqrstuvvwxyz')
    for i in range(26):
        if (ch == letters[i]):
            return letters[(i+13)%26]
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(26):
        if(ch == upper[i]):
            return upper[(i+13)%26]





