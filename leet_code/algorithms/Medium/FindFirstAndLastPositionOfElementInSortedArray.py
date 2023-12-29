# 34. Find First and Last Position of Element in Sorted Array
'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    # 77ms, Beats 88.85%
    # 18.89MB, Beats 5.69%
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first_occurrence(nums, target):
            l = 0
            r = len(nums) - 1
            first_occurrence = -1

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    first_occurrence = m
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return first_occurrence


        def find_last_occurrence(nums, target):
            l = 0
            r = len(nums) - 1
            last_occurrence = -1

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    last_occurrence = m
                    l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return last_occurrence

        first = find_first_occurrence(nums, target)
        last = find_last_occurrence(nums, target)

        return [first, last]