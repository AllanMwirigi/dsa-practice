# given two strings s1='1,1,1' and s2='2,2,2', sum the two strings to provide '333
# not allowed to convert the whole string to int

# similar to https://leetcode.com/problems/add-strings/
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

# note ord(0) = 48

def sumStrings(num1='', num2=''):
    pos1 = len(num1) - 1
    pos2 = len(num2) - 1
    carry = 0
    result = ''

    while pos1 >= 0 or pos2 >= 0:
        n1 = 0
        n2 = 0
        if pos1 >= 0:
            n1 = ord(num1[pos1]) - 48
            pos1 -= 1

        if pos2 >= 0:
            n2 = ord(num2[pos2]) - 48
            pos2 -= 1

        sum = n1 + n2 + carry
        if sum > 9:
            carry = 1
            sum -= 10
        else:
            carry = 0

        #  only need last digit
        result = str(sum) + result

    if carry > 0:
        result = '1' + result

    return result

print(sumStrings("456","57"))

        
