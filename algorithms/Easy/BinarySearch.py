# 704. Binary Search
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    # 184ms, Beats 99.54%
    # 18.84MB, Beats 5.53%
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l)//2
            
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
