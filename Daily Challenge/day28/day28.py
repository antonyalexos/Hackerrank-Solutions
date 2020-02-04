#!/bin/python3

import math
import os
import random
import re
import sys

lst = []
if __name__ == '__main__':
    N = int(input())
    
    for N_itr in range(N):
        firstNameEmailID = input().split()
        
        firstName = firstNameEmailID[0]
        
        emailID = firstNameEmailID[1]
        
        if "@gmail.com" in emailID:
            lst.append(firstName)
lst.sort()
for j in lst:
    print(j)
