'''-----Left Rotation:Given a  2D Array, :

A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.------'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    l=[]
    for i in range(0,d):
        x=a
        s=x.pop(0)
        l.append(s)
    x.extend(l) 
    k=" ".join(str(m) for m in x)   
    print(k)
