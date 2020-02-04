#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a,n):
    cnt = 0
    for i in range(0,n):
        for j in range(0,n-1):
            #Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                cnt+=1
                a[j], a[j + 1] = a[j+1], a[j]
    print("Array is sorted in",cnt ,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])


if __name__ == '__main__':
    n = int(input())
    
    a = list(map(int, input().rstrip().split()))
    
    countSwaps(a,n)
