# 136. Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    # 123 ms, faster than 99.54%
    # 17.2 MB, less than 5.88%
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)