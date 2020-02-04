#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def findMedian(d, nums) -> int :
    a = d//2
    b = a+1
    median1 = None
    median2 = None
    Sum = 0
    
    for i in range(201):
        Sum += nums[i]
        if(Sum >= a and median1 is None):
            median1 = i
        if(Sum >= b):
            median2 = i
            break

if(d%2 == 0):
    return(median1+median2)/2.0
    else:
        return(median2)

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d, n):
    nums = [0]*201
    trail = []
    cnt = 0
    for val in expenditure[:d]:
        nums[val]+=1
        trail.append(val)
    
    for i in range(d,n):
        median = findMedian(d, nums)
        
        if(expenditure[i]>=(2*median)):
            cnt+=1
        trail.append(expenditure[i])
        nums[expenditure[i]]+=1
        temp = trail.pop(0)
        nums[temp]-=1
    
    print(cnt)

if __name__ == '__main__':
    nd = input().split()
    
    n = int(nd[0])
    
    d = int(nd[1])
    
    expenditure = list(map(int, input().rstrip().split()))
    
    activityNotifications(expenditure, d, n)
