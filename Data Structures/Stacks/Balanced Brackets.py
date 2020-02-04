#!/bin/python

import sys
k=0

t = int(raw_input().strip())
for a0 in xrange(t):
    k=0
    s = raw_input().strip()
    length = len(s)
    
    for i in range(length-1):
        if((s[0]=='}') or (s[0]==']') or (s[0]==')')):
            k=0
            break
        if((s[length-1]=='[') or (s[length-1]=='{') or (s[length-1]=='(')):
            k=0
            break
        if((s[i]=='{') and (((s[i+1]==']')) or ((s[i+1]==')')))):
            k=0
            break
        elif((s[i]=='(') and (((s[i+1]==']')) or ((s[i+1]=='}')))):
            k=0
            break
        elif((s[i]=='[') and (((s[i+1]=='}')) or ((s[i+1]==')')))):
            k=0
            break
        else:
            k=1
            continue

if k==1:
    print "YES"
    else:
        print "NO"
#############################################################

lefts = '{[('
rights = '}])'
closes = { a:b for a,b in zip(rights,lefts)}

def valid(s):
    stack = []
    for c in s:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack.pop() != closes[c]:
                return False
    return not stack  # stack must be empty at the end

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if valid(s):
        print 'YES'
    else:
        print 'NO'