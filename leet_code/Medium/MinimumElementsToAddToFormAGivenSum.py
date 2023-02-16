# 1785. Minimum Elements to Add to Form a Given Sum
'''
You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.
Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.
Note that abs(x) equals x if x >= 0, and -x otherwise.
'''


class Solution:
    # 774 ms, faster than 85.16%
    # 26.4 MB, less than 89.84%
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums)-goal) + (limit-1))//limit
