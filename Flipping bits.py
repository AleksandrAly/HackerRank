import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    n_bin = bin(n)
    n_bin = str(n_bin)
    n_bin = n_bin[2:]
    list_n = [0] * (32 - len(n_bin))
    list_n.append(n_bin)
    list_n = ''.join(map(str, list_n))
    list_n = list(list_n)
    i = 0
    while i < 32:
        if list_n[i] == '1':
            list_n[i] = 0
        else:
            list_n[i] = 1
        i += 1
    list_n_rev = ''.join(map(str, list_n))
    rev_num = int(list_n_rev, 2)
    return rev_num
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    result = flippingBits(n)

        #fptr.write(str(result) + '\n')

    #fptr.close()
