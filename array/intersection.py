# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

from typing import List

# T - O(n + m); S -> O(n)
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set(nums1)
    result = []
    for num in nums2:
        if num in nums1_set:
            result.append(num)
            nums1_set.remove(num)
    
    return result

# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_dict = {}
    result = []
    for num in nums1:
        nums1_dict[num] = 1 + nums1_dict.get(num, 0)

    for num in nums2:
        if num in nums1_dict:
            result.append(num)
            nums1_dict[num] -= 1
            if nums1_dict[num] == 0:
                nums1_dict.pop(num)

    return result