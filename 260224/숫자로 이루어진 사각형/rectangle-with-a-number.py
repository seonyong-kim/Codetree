n = int(input())

# Please write your code here.
a = 0    
for i in range(n):
    for j in range(n):
        a += 1
        if a > 9:
            a -= 9
        print(a, end=" ")
    print()