n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abs(arr):
    for i in arr:
        if(i<0):
            i *= (-1)
        print(i, end=" ")

abs(arr)