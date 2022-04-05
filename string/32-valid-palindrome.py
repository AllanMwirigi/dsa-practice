# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# O(1) space
# m_adam
# l - 2
# r - 4
def isPalindrome(s: str):
    left = 0
    right = len(s) - 1
    while right > left:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    
    return True

print(isPalindrome('m_adam'))

def alphaNum(c):
    return (
        ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
    )
        

# takes extra space O(n); uses inbuilt funcs
def isPalindrome2(s: str):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    
    return newStr == newStr[::-1]