import math
import os
import random
import re
import sys

# first solution
def hourgl_Sum(arr):
    max_sum = -100
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            cur_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] \
                      + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum = 0
    return max_sum


# second solution
def hourglass_Sum(arr):
    arr_sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            cur_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] \
                      + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            arr_sum.append(cur_sum)
    return max(arr_sum)


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result_1 = hourgl_Sum(arr)
    result_2 = hourglass_Sum(arr)
    print(result_1, result_2)
