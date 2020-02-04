


#!/bin/python3

import math
import os
import random
import re
import sys


def merge(l1,l2):
    l = []
    global count
    while l1 and l2:
        if l1[-1] <= l2[-1]:
            l.append(l2.pop())
        else:
            l.append(l1.pop())
            count += len(l2)
    l.reverse()
    return l1 + l2 + l

# Complete the countInversions function below.
def countInversions(arr):
    t = len(arr) // 2
    return merge(countInversions(arr[:t]), countInversions(arr[t:])) if t > 0 else arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        count = 0
        
        arr = list(map(int, input().rstrip().split()))
        
        result = countInversions(arr)
        
        fptr.write(str(count) + '\n')
    
    fptr.close()
