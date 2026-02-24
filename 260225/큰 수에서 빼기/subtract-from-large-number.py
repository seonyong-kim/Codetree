arr = input().split()
A, B = int(arr[0]), int(arr[1])

if A > B:
    print(A-B)
else:
    print(B-A)