import sys

strings = []
lines = []
metritis = 0
j = 0

number = int(raw_input())
for i in range(0, number):
    strings.append(raw_input().strip())

queries = int(raw_input())
for i in range(0, queries):
    lines.append(raw_input().strip())

for metritis in lines:
    print strings.count(metritis)



