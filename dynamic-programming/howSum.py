# write a fuction howSum(targetSum, numbers) where numbers is an array
# should return an array containing any combination of elems that add up to exactly the targetSum
# if there is no combination possible, return null
# if multiple combinations possible, may return any single one
# may use an element of the array as many times a needed

def howSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        newTarget = targetSum - num
        result = howSum(newTarget, numbers, memo)
        if result is not None:
            # latest = result + [result]
            result.append(num)
            memo[targetSum] = result
            return memo[targetSum]

    memo[targetSum] = None
    return None

print(howSum(7, [5, 3, 4, 7]))
# print(howSum(8, [2, 4]))
# print(howSum(300, [7, 14]))