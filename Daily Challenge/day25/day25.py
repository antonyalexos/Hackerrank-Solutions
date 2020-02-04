import sys

numbers = int(input())
flag = True
for _ in range(0,numbers):
    i = int(input())
    if(i<2):
        flag = False
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            flag = False
            break
    if(flag): print("Prime")
    else: print("Not prime")
    flag = True
