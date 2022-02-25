import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    arr = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_UP = alphabet.upper()
    for i in range(len(s)):
        if s[i] in alphabet:
            index_i = alphabet.index(s[i])
            new_ind = (index_i + k) % 26
            arr.append(alphabet[new_ind])

        elif s[i] in alphabet_UP:
            index_i = alphabet_UP.index(s[i])
            new_ind = (index_i + k) % 26
            arr.append(alphabet_UP[new_ind])

        else:
            arr.append(s[i])

    return ''.join(arr)


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
#    fptr.write(result + '\n')

#    fptr.close()
