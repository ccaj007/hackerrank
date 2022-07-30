import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    max_value = 0
    tmp = 0

    while n > 0:
        if n % 2 == 1:
            tmp += 1
            if tmp > max_value:
                max_value = tmp
        else:
            tmp = 0

        n //=2
    print(max_value)


