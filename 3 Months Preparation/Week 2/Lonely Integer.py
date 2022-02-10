import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    sum_par = 0
    for i in range(n):
        for b in range(n):
            if i != b and a[i] == a[b]:
                sum_par += a[b]  #It's work only for elements that occur twice (not thrice or more)
    answer = sum(a) - sum_par
    return answer

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = lonelyinteger(a)
print(result)
#    fptr.write(str(result) + '\n')

#    fptr.close()
