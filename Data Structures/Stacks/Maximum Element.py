# Enter your code here. Read input from STDIN. Print output to STDOUT
Stack = []
N = int(raw_input())
maximum = [0]

for i in range(N):
    query = map(int,raw_input().strip().split(' '))
    if query[0]==1:
        Stack.append(query[1])
        if(query[1]>maximum[-1]):
            maximum.append(query[1])
    elif query[0]==2:
        if (Stack.pop()==maximum[-1]):
            maximum.pop()
    elif query[0]==3:
        print maximum[-1]

