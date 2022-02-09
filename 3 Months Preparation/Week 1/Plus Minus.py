import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pls = 0
    mns = 0
    nll = 0
    for i in range(n):
        if arr[i] > 0:
            pls += 1
        elif arr[i] < 0:
            mns += 1
        elif arr[i] == 0:
            nll += 1
    val_pls = pls / n
    val_mns = mns / n
    val_nll = nll / n
    val_pls = "%.6f" % val_pls
    val_mns, val_nll = "%.6f" % val_mns, val_nll
    val_nll = "%.6f" % val_nll
    print(val_pls, val_mns, val_nll, sep='\n')
    return

    # Write your code here

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
