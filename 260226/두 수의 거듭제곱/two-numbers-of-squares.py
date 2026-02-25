a, b = map(int, input().split())

# Please write your code here.
prod = 1
while b > 0:
    prod *= a
    b-=1
    
print(prod)