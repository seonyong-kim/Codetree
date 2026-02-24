n = int(input())

# Please write your code here.

def sum(n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum

print(sum(n)//10)