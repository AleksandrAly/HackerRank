import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    arr.sort()
    brr.sort()
    res = 0
    for i in range(arr[-1], brr[0] + 1):
        # if all(i % x == 0 for x in arr) and all(x % i == 0 for x in brr):   # "short" solution
            # res += 1
        for ai in range(n):
            if i % arr[ai] != 0:
                break
            if ai == n - 1:
                for bi in range(m):
                    if brr[bi] % i != 0:
                        break
                    if bi == m - 1:
                        res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()