# 287. Find the Duplicate Number
'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
'''

class Solution:
    # 435ms, Beats 97.95%
    # 36.51MB, Beats 7.94%
    def findDuplicate(self, nums: List[int]) -> int:
        data = {}

        for i in nums:
            if i in data:
                return i
            else:
                data[i] = 1