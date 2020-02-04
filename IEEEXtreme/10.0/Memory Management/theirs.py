T = input()
for t in range(T):
    P,S,N = map(int, raw_input().split())
    # memoryAddresses =[]
    
    pagesFIFO=[]
    pagesLRU=[]
    for i in range(P):
        pagesFIFO.append('')
        pagesLRU.append('')
    
    
    changersinFIFO=0
    changersinLRU=0
    # print pagesFIFO
    for n in range(N):
        # memoryAddresses.append(input())
        requestedLocation=input()/S
        # print requestedLocation,"request....",
        #
        # print pagesFIFO,pagesLRU
        # ___________________________________________
        if requestedLocation not in pagesFIFO:
            # print "not in pagesFIFO"
            if '' not in pagesFIFO:
                changersinFIFO+=1
            pagesFIFO.pop(0)
            pagesFIFO.append(requestedLocation)
        # else:
        # print "in pagesFIFO"
        # ___________________________________________
        if requestedLocation not in pagesLRU:
            # print "not in pagesLRU"
            if '' not in pagesLRU:
                changersinLRU+=1
            pagesLRU.pop(0)
            pagesLRU.append(requestedLocation)
        else:
            pagesLRU.remove(requestedLocation)
            pagesLRU.append(requestedLocation)
# print "in pagesLRU"
# ___________________________________________
# print pagesFIFO,pagesLRU

if changersinLRU<changersinFIFO:
    print "yes",
else:
    print "no",
print changersinFIFO,changersinLRU


