import math
import os
import random
import re
import sys



#if __name__ == '__main__':
n = int(input().strip())

a = list(map(int, input().rstrip().split()))

    # Write your code here
numSwaps = 0
for i in range(n):
    for j in range(n):
        if (a[i] < a[j]) and (i > j):
            a[i], a[j] = a[j], a[i]
            numSwaps += 1
            print(a, numSwaps)
print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element:", a[0])
print("Last Element:", a[n-1])
