a, b = map(int, input().split())

# Please write your code here.
def checkOn(a,b):
    count = 0
    for i in range(a,b+1):
        if(i % 2 != 0 and i%10 != 5):
            if (i%3 == 0 and i%9 != 0):
                continue
            count += 1
    return count


print(checkOn(a,b))