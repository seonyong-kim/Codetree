n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def div_2 (arr):
    n=0
    for i in arr:
        if(i%2==0):
            arr[n] = int(arr[n] / 2)
        n+=1
    
    for i in arr:
        print(i, end=" ")

div_2(arr)

