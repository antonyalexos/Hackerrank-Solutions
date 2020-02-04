func = [[[0 for k in range(510)] for j in range(255)] for i in range(255)]


def Palindrome(word, N):
    length = len(word)
    num = (length+1)//2
    mismatches = 0
    for i in range(num):
        if(word[i] != word[length-i-1]):
            mismatches += 1
    func[0][0][0] = 1
    
    for n in range(N+1):
        for k in range(1,num+1):
            for b in range(mismatches+1):
                if(k-1 == length - k):
                    func[n][k][b] = func[n][k-1][b]
                    if(n>=1):
                        func[n][k][b] = (func[n][k][b] + 25 * func[n-1][k-1][b]) % 1000000007
                elif(word[k-1] == word[length-k]):
                    func[n][k][b] = func[n][k-1][b]
                    if(n>=2):
                        func[n][k][b] = (func[n][k][b] + 25 * func[n-2][k-1][b]) % 1000000007
                elif(word[k-1] != word[length-k]):
                    if(b>=1 and n>=1):
                        func[n][k][b] = 2 * func[n-1][k-1][b-1]
                    if(n>=2):
                        func[n][k][b] = (func[n][k][b] + 24 * func[n-2][k-1][b-1]) % 1000000007
    return func[N][num][mismatches]

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        n, word = input().split(maxsplit=1)
        n = int(n)
        # test = Palindrome(word, n)
        print(int(Palindrome(word, n)))
