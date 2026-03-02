arr = input().split()
a,b = int(arr[0]), int(arr[1])

def checkEven(a):
    if(a%2 == 0):
        print("even")
    else:
        print("odd")

checkEven(a)
checkEven(b)