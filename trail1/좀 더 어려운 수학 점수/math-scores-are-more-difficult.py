math_A, english_A = map(int, input().split())
math_B, english_B = map(int, input().split())

if(math_A > math_B):
    print("A")
elif(math_A < math_B):
    print("B")
else:
    if(english_A > english_B):
        print("A")
    elif(english_A < english_B):
        print("B")