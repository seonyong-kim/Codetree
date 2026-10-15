A = input()

# Please write your code here.
def isPalindrome(str):
    n = len(str)
    result = "Yes"
    for i in range(n//2):
        if(str[i] != str[n-1-i]):
            result = "No"
            break
    print(result)

isPalindrome(A)