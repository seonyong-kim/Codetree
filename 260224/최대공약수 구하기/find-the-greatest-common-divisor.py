n, m = map(int, input().split())

# Please write your code here.
def GCD(n,m):
    max = 0
    if n > m:
        min = m
    else:
        min = n
    
    for i in range(2,min):
        if(n % i == 0 & m & i == 0):
            max = i
    
    print(max)

GCD(n,m)