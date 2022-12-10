#!/bin/python3

import math
import os
import random
import re
import sys

test = """
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
"""

nm = test.split()
print(nm)
n = int(nm[0])
m = int(nm[1])
k = int(nm[-1])
arr = []
newnm = nm[2:-1]

print(n, m, k)
print(newnm)
# t=newnm[0:3]
# arr.append(t)
# print(arr)
# t=newnm[3:6]
# arr.append(t)
# print(arr[1])

j = 0
for x in range(n):
    t = []
    for i in range(m):

        t.append(int(newnm[j]))
        j += 1

    arr.append(t)
#    arr[x]=t

print(arr)
print('result')
arr.sort(key = lambda row: row[k])
for i in arr:
    for j in i:
        print(j,end=" ")
    print("")
