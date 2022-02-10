
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.replace(' ', '')  # string without spaces
    if len(s) < 26:     # exclude extra work
        answer = 'not pangram'
        return answer
    s = s.lower()
    uniq_lett = 0
    for i in range(97, 123):
        i = "{:c}".format(i)  # in this range we can change i from numbers to alphabet letters
        n = 0
        while n < len(s):
            if s[n] == i:
                uniq_lett += 1
                n = len(s)
            else:
                n += 1
    if uniq_lett == 26:
        answer = 'pangram'
    else:
        answer = 'not pangram'
    return answer
#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = pangrams(s)
print(result)

    #fptr.write(result + '\n')

    #fptr.close()
