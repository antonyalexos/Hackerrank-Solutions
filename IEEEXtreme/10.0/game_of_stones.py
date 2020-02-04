test_cases = int(input())
for i in range(test_cases):
    games = int(input())
    sum = 0
    for j in range(games):
        piles_num = int(input())
        pile = [int(i) for i in input().split()]
        for j in range(piles_num):
            sum = sum + pile[j]//2
    if(sum%2!=0):
        print("Alice")
else:
    print("Bob")
