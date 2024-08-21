def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
p = input("Enter a string: ")
if is_palindrome(p):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


#Short method
# if(p == p[::-1]):