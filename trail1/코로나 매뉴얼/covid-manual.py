import sys

arr = [line.split() for line in sys.stdin]
number = 0
for i in arr:
    if(i[0] == "Y" and int(i[1]) >= 37):
        number +=1

if(number >= 2):
    print("E")
else:
    print("N")