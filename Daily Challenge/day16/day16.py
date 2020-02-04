#!/bin/python3

import sys


S = input().strip()
try:
    x = int(S)
except ValueError:
    print ("Bad String")
print (x)


