n, m = map(int, input().split())

# Please write your code here.
def findLCM(n,m):
    LCM = 10000
    for i in range(max(n,m),10000):
        if(i % n == 0 and i % m == 0):
            LCM = i
            break

    print(LCM)

findLCM(n,m)
