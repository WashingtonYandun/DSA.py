# 189. Rotate Array
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''


class Solution:
    # 3279 ms, faster than 5.00%
    # 24 MB, less than 99.72%
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # need to improve this solution
        for i in range(k):
            mk = nums.pop()
            nums.insert(0,mk)