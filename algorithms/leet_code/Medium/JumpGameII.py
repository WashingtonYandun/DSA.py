# 45. Jump Game II
'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
'''


class Solution:
    # 239 ms, faster than 50.59%
    # 15.1 MB, less than 59.20%
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0

        # traverse all the list
        while r < len(nums) - 1:
            farthest = 0

            # traverse each of the sublists
            for pos in range(l, r + 1, 1):
                farthest = max(farthest, pos + nums[pos])

            l = r + 1
            r = farthest

            jumps = jumps + 1

        return jumps
