a, b = map(int, input().split())

# Please write your code here.
def checkPrime(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def countPrime(a,b):
    sum = 0
    for i in range(a,b+1):
        if(checkPrime(i)):
            sum += i
    return sum

print(countPrime(a,b))