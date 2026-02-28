M, D = map(int, input().split())

# Please write your code here.
def checkCal(M,D):
    if M < 1 or M > 12:
        return "No"
    elif M == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if(D > 0 and D <32):
            return "Yes"
        else:
            return "No"
    elif M == 2:
        if D >= 1 and D <= 28:
            return "Yes"
        else:
            return "No"
    else:
        if D >= 1 and D <= 30:
            return "Yes"
        else:
            return "No"

print(checkCal(M,D))    