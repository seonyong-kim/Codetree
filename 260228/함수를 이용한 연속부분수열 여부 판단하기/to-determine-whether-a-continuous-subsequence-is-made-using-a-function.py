n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def contain_sublist(lis, sub):
    n, m = len(lis), len(sub)
    if m > n:
        return "No"
    for i in range(n-m+1):
        if lis[i:i+m] == sub:
            return "Yes"
    return "No"

print(contain_sublist(a,b))