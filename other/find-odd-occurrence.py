# Given an array of positive integers. All numbers occur an even number of times except one. 
# Find the number in O(n) time & constant space.

# hashmap soln will use O(n space)

# do bitwise XOR of all the elements. XOR of all elements gives us odd occurring elements. 
# Note: XOR of two elements is 0 if both elements are the same  (XOR of number with itself is 0)
#       XOR of a number x with 0 is x.
# XOR of num even number of times is 0 i.e. 5 XOR 5 XOR 5 XOR 5 = 0
# therefore: XOR of num with itself odd number of times is itself i.e. 5 XOR 5 XOR 5 = 5
# XOR is associative and commutative i.e. (A XOR B) XOR C == A XOR (B XOR C)
def findOddOccurrence(numbers):
    result = 0
    for num in numbers:
        result = result ^ num

    return result

# arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
arr = [2, 7, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2, 7, 4, 4, 5]
print(findOddOccurrence(arr))