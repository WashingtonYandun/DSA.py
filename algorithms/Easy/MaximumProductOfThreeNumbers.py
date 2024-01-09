# 628. Maximum Product of Three Numbers
'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
'''

class Solution:
    # 205ms Beats 100.00%
    # 18.69MB Beats 33.10%
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_product = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        return max_product