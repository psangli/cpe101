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
import char
def str_rot_13(ch):
    string = list(ch)
    for i in range(len(string)):
        string[i] = char.rot_13(string[i]);
    return join(string)

def str_translate_101(string, old, new):
    array = list(string)
    for i in range(len(array)):
        if (array[i] == old):
            array[i] = new
    return join(array)

def join(arr):
    string = '';
    for i in arr:
        string= string + i
    return string

