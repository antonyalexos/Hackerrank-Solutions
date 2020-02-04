import sys


n = int(raw_input().strip())
binary = bin(n)
counter = 0
final = 0

for i in str(binary[2:]):
    if(int(i)==1):
        counter += 1
    elif(int(i)==0):
        counter = 0
    if(counter > final):
        final = counter
print final