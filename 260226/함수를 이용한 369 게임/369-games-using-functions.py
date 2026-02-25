a, b = map(int, input().split())

# Please write your code here.
def check369(m):
    if '3' in str(m):
        return True
    elif '6' in str(m):
        return True
    elif '9' in str(m):
        return True
    else:
        return False

def count3(a,b):
    count = 0
    for i in range(a,b+1):
        if(i%3==0 or check369(i)):
            count+=1
    return count

print(count3(a,b))    