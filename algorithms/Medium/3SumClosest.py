# 16. 3Sum Closest
'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


import math

class Solution:

    # 718msBeats 87.81%of users with Python3
    # 16.30mb Beats 97.67%of users with Python3
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = math.inf
        nums.sort() # to pointers aproach
        n = len(nums)

        for i in range(n - 2):
            l =  i + 1
            r = n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    l += 1
                else:
                    r -=1

                if abs(total - target) < abs(closest - target):
                    closest = total
                    
        return closest
