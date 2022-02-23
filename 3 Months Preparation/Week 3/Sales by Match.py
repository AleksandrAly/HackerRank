import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    every_color = [0] * (max(ar) + 1)
    one_pair = []
    for i in ar:
        every_color[i] += 1
    for i in range(len(every_color)):
        one_pair.append(every_color[i] // 2)
    pairs = sum(one_pair)
    return pairs


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
