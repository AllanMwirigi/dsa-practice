# https://leetcode.com/problems/two-sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict() # diff: index
        for i, num in enumerate(nums):
            if num in diffs: # current num is a diff of a previous elem
                return [diffs[num], i]
            diff = target - num
            diffs[diff] = i # map diff of num from target and its index

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                sum = nums[i] + nums[j]
                if (sum == target):
                    return [i, j]
        