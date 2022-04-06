# given a sorted array, find the two numbers that give a sum closest to x

def closestSum(numbers, target):
    n = len(numbers)
    l = 0
    r = n - 1
#    Diff is used to store the difference between pair and target. We need to find the minimum diff.
    diff = float('inf')
    best_l = l
    best_r = r

    # While there are elements between l and r
    while r > l:
        sum = numbers[l] + numbers[r]
        if abs(sum - target) < diff:
            best_l = l
            best_r = r
            diff = abs(sum - target)

        # If this pair exceeds target, move to smaller values.
        if sum > target:
            r -= 1
        else:
            l += 1

    return [numbers[best_l], numbers[best_r]]


# bestSum
# sum each pair
# find value <= target, > bestsum
# 8 - [1, 2, 4, 5, 10, 15]
# closest - 7
# O(Nsq)
def closestSum2(numbers, target):
    n = len(numbers)
    closest_sum = float('-inf')
    best = []
    for i in range(n):
        for j in range(n):
            if i != j:
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [numbers[i], numbers[j]]
                if sum < target and sum > closest_sum:
                    closest_sum = sum
                    best = [numbers[i], numbers[j]]

    return best

# arr = [1, 2, 4, 5, 10, 15]
# print(closestSum(arr, 8))
arr = [10, 22, 28, 29, 30, 40]
print(closestSum(arr, 54))

