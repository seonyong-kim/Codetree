Y, M, D = map(int, input().split())

# Please write your code here.
def checkYear(Y):
    if(Y%4 == 0):
        if(Y % 100 == 0):
            if(Y % 400 == 0):
                return True
            else:
                return False
            return False
        return True
    return False

def CheckSeason(M):
    if(M in [12,1,2]):
        return "Winter"
    elif(M in [3,4,5]):
        return "Spring"
    elif(M in [6,7,8]):
        return "Summer"
    else:
        return "Fall"

def check(Y,M,D):
    Yun = checkYear(Y)
    if(M in [4,6,9,11] and D <= 30 and D >= 1):
        print(CheckSeason(M))
    elif(M == 2 and D >= 1):
        if(Yun and D <= 29):
            print(CheckSeason(M))
        elif(not Yun and D <= 28):
            print(CheckSeason(M))
        else:
            print(-1)
    elif(M in [1,3,5,7,8,10,12] and D >= 1 and D <= 31):
        print(CheckSeason(M))
    else:
        print(-1)

check(Y,M,D)