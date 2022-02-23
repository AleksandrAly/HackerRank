#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    sides = []
    while sticks[-1] >= sticks[-2] + sticks[-3] and len(sticks) > 3:
        sticks = sticks[:-1]
    if sticks[-1] >= sticks[-2] + sticks[-3]:
        sides.append(-1)
    else:
        sides = sticks[-3:]
    return sides


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(result)
    
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
