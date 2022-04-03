# https://leetcode.com/problems/permutations/
# https://www.youtube.com/watch?v=s7AvT7cGdSo
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums):
    result = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        num = nums[i]
        perms = permute(nums[:i] + nums[i+1:]) # ?
        for perm in perms:
            perm.append(num)
        result.extend(perms)

    return result

print(permute([1,2,3]))
