n = int(input())

# Please write your code here.
def digitSum(n):
    return n//10 + n%10

if(n%2==0 and digitSum(n)%5==0):
    print("Yes")
else:
    print("No")