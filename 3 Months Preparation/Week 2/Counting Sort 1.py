import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    freq_arr = [0] * 100
    for i in range(0, 100):
        for numbers in arr:
            if numbers == i:
                freq_arr[i] += 1
    return freq_arr
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = countingSort(arr)
print(result)

#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()
