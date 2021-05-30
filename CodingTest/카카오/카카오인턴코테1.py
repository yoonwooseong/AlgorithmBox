import itertools


def diverseDeputation(m, w):
    # Write your code here
    result = 0
    if m == 0 or w == 0:
        print(0)
    else:

        for i in range(1, m+1):
            if 3 - i > 0:
                mlist = list(itertools.combinations(range(m), i))
                wlist = list(itertools.combinations(range(w), 3-i))
                print(mlist)
                print(wlist)
                lenm = len(mlist)
                lenw = len(wlist)
                print(lenm, lenw)
                result += (lenm * lenw)

        print(result)


diverseDeputation(4, 9)

'''
#!/bin/python3

import math
import os
import random
import re
import sys


import itertools
#
# Complete the 'diverseDeputation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER w
#

def diverseDeputation(m, w):
    # Write your code here
    result = 0
    if m == 0 or w == 0:
        return 0
    else:
        for i in range(1, m+1):
            if 3 - i > 0:
                lenm = len(list(itertools.combinations(range(m), i)))
                lenw = len(list(itertools.combinations(range(w), 3-i)))
                result += (lenm * lenw)
        return result

if __name__ == '__main__':
'''
