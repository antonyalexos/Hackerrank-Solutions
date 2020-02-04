from collections import deque

test_cases = int(input())
for i in range(test_cases):
    p, s, n = [int(i) for i in input().split()]
    fifo = []
    lru = []
    for i in range(p):
        fifo.append('')
        lru.append('')
    fifo_counter = 0
    lru_counter = 0;
    for i in range(n):
        number = int(input())
        number = number//s
        
        if(number not in fifo):
            if '' not in fifo:
                fifo_counter+=1
            fifo.pop(0)
            fifo.append(number)
        
        if(number not in lru):
            if '' not in lru:
                lru_counter+=1
            lru.pop(0)
            lru.append(number)
        elif(number in lru):
            lru.remove(number)
            lru.append(number)

fifo.clear()
lru.clear()
if(lru_counter < fifo_counter):
    print("yes", fifo_counter, lru_counter)
    else:
        print("no", fifo_counter, lru_counter)
