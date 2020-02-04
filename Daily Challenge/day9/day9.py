fac = int(raw_input())
def factorial(fac):
    if(fac>1):
        return fac*(factorial(fac-1))
    elif(fac==1):
        return 1

print factorial(fac)