# Maximum Subarray
'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
'''


class Solution:
    # 828 ms, Beats 29.91%
    # 28.6 MB, Beats 43.90%
    def maxSubArray(self, nums: List[int]) -> int:
        max_relative = nums[0]
        max_general = nums[0]

        for i in range(1, len(nums), 1):
            max_relative = max(nums[i], max_relative + nums[i])
            max_general = max(max_general, max_relative)

        return max_general
