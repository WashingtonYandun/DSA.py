# 1480. Running Sum of 1d Array
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    # 37ms, Beats 93.78%
    # 17.49MB, Beats 12.69%
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums