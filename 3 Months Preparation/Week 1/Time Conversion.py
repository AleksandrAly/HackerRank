import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_24 = s[:-2]
    nl = str(0)
    if s[-2:] == 'PM' and s[:2] == '12':
        time_24 = s[:-2]
    elif s[-2:] == 'PM':
        hours_12 = int(s[:2])
        hours_24 = hours_12 + 12
        if hours_24 > 9:
            time_24 = [str(hours_24), time_24[2:]]
            time_24 = ''.join(time_24)
        else:
            time_24 = [nl, str(hours_24), time_24[2:]]
            time_24 = ''.join(time_24)
    if s[-2:] == 'AM' and s[:2] == '12':
        time_24 = [nl, nl, time_24[2:]]
        time_24 = ''.join(time_24)

    return time_24

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()
result = timeConversion(s)
print(result)
#    fptr.write(result + '\n')

#    fptr.close()
