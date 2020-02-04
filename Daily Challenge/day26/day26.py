import sys

actual = list(map(int, input().split()))
expected = arr = list(map(int, input().split()))

fine = 0

if(expected[2]<actual[2]):
    fine = 10000
elif(expected[2]==actual[2]):
    if(expected[1]<actual[1]):
        fine = (abs(expected[1]-actual[1])*500)
    elif(expected[1]==actual[1]):
        if(expected[0]<actual[0]):
            fine = (abs(expected[0]-actual[0])*15)
print(fine)


