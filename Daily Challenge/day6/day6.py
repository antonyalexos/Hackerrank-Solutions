import sys

cases = 0
string = {"\0"}

cases = int(raw_input())

for x in range(0,cases):
    string = raw_input()
    for i in range(0,len(string)):
        if i%2==0:
            sys.stdout.write(string[i]),
    print " ",
    for j in range(0,len(string)):
        if j%2!=0:
            sys.stdout.write(string[j]),
    print ""

