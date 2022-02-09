
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    coun = [0, 0]
    max_scor = scores[0]
    min_scor = scores[0]
    for i in range(n-1):
        if scores[i+1] > max_scor:
            max_scor = scores[i+1]
            coun[0] += 1
        if scores[i+1] < min_scor:
            min_scor = scores[i+1]
            coun[1] += 1
    return coun
#if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

#    fptr.write(' '.join(map(str, result)))
 #   fptr.write('\n')

#    fptr.close()