# write a fuction bestSum(targetSum, numbers) where numbers is an array
# should return an array containing shortest combination of elems that add up to exactly the targetSum
# if there is no combination possible, return null
# if multiple shortest combinations possible, may return any single one
# may use an element of the array as many times a needed

def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortest = None
    for num in numbers:
        newTarget = targetSum - num
        result = bestSum(newTarget, numbers, memo)
        if result != None:
            # combination.append(num)
            combination = result + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination

    memo[targetSum] = shortest
    return memo[targetSum]

print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]