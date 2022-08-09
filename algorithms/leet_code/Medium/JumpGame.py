# 55. Jump Game
'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''


class Solution:
    # 107 ms, faster than 89.72%
    # 15.1 MB, less than 96.82%
    def canJump(self, nums: List[int]) -> bool:
        # nums[pos] => jums
        # we have to reach 0 index so in python we use one minus number in this case
        target_pos = len(nums) - 1
        for pos in range(target_pos, -1, -1):
            if pos + nums[pos] >= target_pos:
                target_pos = pos

        return target_pos == 0
