import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    num_val = 0
    way = {}
    i = 0
    while i < steps:
        if path[i] == 'U':
            sea_level += 1
        if path[i] == 'D':
            sea_level -= 1
        way[i] = sea_level  #dictionary with sea level for every step
        i += 1
    for i in range(steps - 1):
        if (way[i] >= 0) and (way[i + 1] < 0):  #standart situation for valleys counting
            num_val += 1
    if way[0] < 0: #situation, when we start from valley
        num_val += 1
    return num_val
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

steps = int(input().strip())

path = input()

result = countingValleys(steps, path)
print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()