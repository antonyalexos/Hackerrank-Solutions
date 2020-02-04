# Enter your code here. Read input from STDIN. Print output to STDOUT
seqList = []
lastAns = 0
opt = 0

X = 0
Y = 0

lst = map(int, raw_input().split())
N = lst[0]
Q = lst[1]

for i in range(0,N):
    seqList.append([])

for i in range(0,Q):
    lst= map(int, raw_input().split())
    opt = lst[0]
    X = lst[1]
    Y = lst[2]
    if(opt == 1):
        k = ((X ^ lastAns) % N)
        seqList[k].append(Y)
    elif(opt == 2):
        k = ((X ^ lastAns) % N)
        size = len(seqList[k])
        lastAns = seqList[k][Y % size]
print lastAns