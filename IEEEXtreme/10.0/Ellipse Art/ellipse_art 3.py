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
    x1 = [0] * 50
    y1 = [0] * 50
    x2 = [0] * 50
    y2 = [0] * 50
    r  = [0] * 50
    ellipses = int(input())
    counter = 0
    for j in range(ellipses):
        x1[j],y1[j],x2[j],y2[j],r[j] = [int(i) for i in input().split()]
    
    for h in frange(-50.0,50.0,0.1):
        for w in frange(-50.0,50.0,0.1):
            for l in range(ellipses):
                if((distance(h,w,x1[l],y1[l]))+(distance(h,w,x2[l],y2[l])) <= r[l]):
                    counter += 1
                    break


print((str(round((1000000-counter)/10000)))+'%')
