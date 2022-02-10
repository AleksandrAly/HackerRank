import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    pr_diag = 0
    sec_diag = 0
    for i in range(n):
        pr_diag += arr[i][i]
        sec_diag += arr[i][n-i-1]
    diag_diff = abs(pr_diag - sec_diag)
    return diag_diff

#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()