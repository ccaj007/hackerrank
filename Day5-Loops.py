# https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def get_multiples(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

if __name__ == '__main__':
    n = int(input().strip())

    get_multiples(n)
