# 35. Search Insert Position
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    # 48ms, Beats 88.76%
    # 18.20MB, Beats 5.56%
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l