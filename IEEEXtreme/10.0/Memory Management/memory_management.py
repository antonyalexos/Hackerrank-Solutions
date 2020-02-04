from collections import deque

test_cases = int(input())
for i in range(test_cases):
    p, s, n = [int(i) for i in input().split()]
    fifo = deque(maxlen=p)
    lru = deque(maxlen=p)
    fifo_counter = 0
    lru_counter = 0;
    for i in range(n):
        number = int(input())
        number = number//s
        
        if(i<p):
            fifo.append(number)
        elif(number not in fifo):
            fifo.popleft()
            fifo.append(number)
            fifo_counter+=1
        
        if(i<p):
            lru.append(number)
        elif(number not in lru):
            lru.popleft()
            lru.append(number)
            lru_counter+=1
        elif(number in lru):
            lru.remove(number)
            lru.append(number)

    if(lru_counter < fifo_counter):
        print("yes", fifo_counter, lru_counter)
    else:
        print("no", fifo_counter, lru_counter)

