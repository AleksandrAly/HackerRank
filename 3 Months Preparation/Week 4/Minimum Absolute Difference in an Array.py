import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    min_dif = []
    arr = sorted(arr)
    for i in range(len(arr) - 1):
            dif = abs(arr[i] - arr[i + 1])
            min_dif.append(dif)
    return min(min_dif)


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()