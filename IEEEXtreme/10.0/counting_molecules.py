c, h, o = [int(i) for i in input().split()]

try:
    if(h%2!=0):
        raise Exception
    maxW = h//2
    o -= maxW
    if(o%2!=0):
        raise Exception
    total_C = o//2
    c -= total_C
    if(c%6!=0):
        raise Exception
    total_G = c//6
    total_W = maxW - total_G*6
    if(total_W<0):
        raise Exception
    print(total_W,total_C,total_G)
except Exception:
    print("Error")
