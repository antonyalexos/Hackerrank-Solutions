cases = int(input())
for l in range(cases):
    brushA = 0
    brushB =0
    indexA = 0
    indexB = 0
    nofWalls = int(input())
    colors = [int(i) for i in input().split()]
    
    counter = 0
    current = 0
    indexA = 0
    indexB = 0
    
    for k in range(len(colors)):
        current = colors.pop(0)
        
        if(current== brushA or current== brushB):
            continue
        
        counter+=1
        try:
            indexA = colors.index(brushA)
        except ValueError:
            indexA = 501
        try:
            indexB = colors.index(brushB)
except ValueError:
    indexB = 501
        
        if(indexA<indexB):
            brushB = current
        elif(indexA>indexB):
            brushA = current
    else:
        brushA = current

print(counter)
