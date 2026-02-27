a, b = map(int, input().split())

# Please write your code here.
def isPrime(a):
    for i in range(2,a):
        if(a%i == 0):
            return False
    return True

def countNumber(a,b):
    count = 0
    for i in range(a,b+1):
        if(isPrime(i) == False):
            continue
        if((i // 100 + i // 10 + i % 10) % 2 == 0):
            count +=1
    return count

print(countNumber(a,b))