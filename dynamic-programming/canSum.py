# write a fuction canSum(targetSum, numbers) where numbers is an array
# should return a boolean indicating whether ot not it is possible to generate the targetSum  using numbers from the array
# may use an element of the array as many times a needed
# assume all input numbers are non negative

def canSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        newTarget = targetSum - num
        if canSum(newTarget, numbers) is True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(canSum(7, [5, 3, 4, 7])) # -> true
print(canSum(7, [2, 4])) # false
print(canSum(300, [7, 14])) # false