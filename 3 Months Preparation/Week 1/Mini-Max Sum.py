import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(min_sum, end = " ")
    print(max_sum)
    return
#if __name__ == '__main__':

arr = list(map(int, input().rstrip().split()))
#print(sum(arr), min(arr), max(arr))
miniMaxSum(arr)