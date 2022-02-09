import math
import os
import random
import re
import sys

n = int(input().strip())
arr = list(map(int, input().rstrip().split()[:n]))

arr.reverse()
print(*arr, sep=" ")
