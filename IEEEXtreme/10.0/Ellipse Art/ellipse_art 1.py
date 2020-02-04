def distance(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    dis = ((x**2 + y**2)**(1/2))
    return(dis)

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

cases = int(input())
for k in range(cases):
    ellipses = int(input())
    counter = 0
    array = [ [0] * 100 for _ in range(100)]
    for j in range(ellipses):
        
        x1,y1,x2,y2,r = [int(i) for i in input().split()]
        
        for h in frange(-50.0,50.0,0.1):
            for w in frange(-50.0,50.0,0.1):
                if(array[h][w] != 1):
                    if((distance(h,w,x1,y1))+(distance(h,w,x2,y2)) <= r):
                        array[h][w] = 1
                        counter +=1

print((str((10000-counter)//100))+'%')





