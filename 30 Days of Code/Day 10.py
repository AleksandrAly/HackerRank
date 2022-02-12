import math
import os
import random
import re
import sys


def Num_1(n):
    n_bin = str(bin(n))[2:]
    max_len_1 = 0
    len_1 = 0
    n_bin = list(n_bin)
    for i in range(len(n_bin)):
        if n_bin[i] == '1':
            len_1 += 1
        if n_bin[i] == '0':
            if len_1 > max_len_1:
                max_len_1 = len_1
            len_1 = 0
        else:
            if len_1 > max_len_1:
                max_len_1 = len_1
    return max_len_1


if __name__ == '__main__':
    n = int(input().strip())
    result = Num_1(n)
    print(result)
