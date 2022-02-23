import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    for i in range(len(s) // 2):
        start_num = int(s[:i + 1])
        test_s = str(start_num)
        num = start_num
        while len(test_s) < len(s):
            num += 1
            test_s += str(num)
            if s == test_s:
                return print("YES", start_num)
    return print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
