#!/bin/python3


N = int(input().strip())

if (N % 2 == 1) or (5 < N < 21):
    print('Weird')
else:
    print('Not Weird')
