from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return "{} {} ".format(self.name, self.score)
    
    def comparator(a, b):
        for i in range(0,n):
            for j in range(0,n-1):
                #Swap adjacent elements if they are in decreasing order
                if (a.score > b.score):
                    return -1
                elif (a.score == b.score):
                    if(a.name>b.name):
                        return 1
                    else:
                        return -1
        else:
            return 1     
