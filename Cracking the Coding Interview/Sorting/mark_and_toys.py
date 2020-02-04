#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k, n):
    prices.sort()
    cnt = 0
    
    for i in range(0,n):
        k-=prices[i]
        if(k>= 0):
            cnt+=1
        else:
            break
    return(cnt)

if __name__ == '__main__':
    
    nk = input().split()
    
    n = int(nk[0])
    
    k = int(nk[1])
    
    prices = list(map(int, input().rstrip().split()))
    
    result = maximumToys(prices, k, n)
    
    print(result)



