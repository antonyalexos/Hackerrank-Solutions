#!/bin/python

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

sh1 = sum(h1)
sh2 = sum(h2)
sh3 = sum(h3)

while(1):
    
    if(sh1==sh2 and sh2==sh3):
        break
    
    maximum = max(sh1,sh2,sh3)
    
    if(sh1==maximum):
        sh1 = sh1 - h1[0]
        del h1[0]
    elif(sh2==maximum):
        sh2 = sh2 - h2[0]
        del h2[0]
    elif(sh3==maximum):
        sh3 = sh3 - h3[0]
        del h3[0]

    
print sh1
 
