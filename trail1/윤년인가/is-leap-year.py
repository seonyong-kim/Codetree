X = int(input())
if(X%4 == 0):
    if(X%100 == 0 and X%400 != 0):
        print("false")
    else:
        print("true")
else:
    print("false")