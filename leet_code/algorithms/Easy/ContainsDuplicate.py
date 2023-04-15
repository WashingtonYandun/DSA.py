# 217. Contains Duplicate
'''
Given an integer array nums,
return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


class Solution:
    # 477 ms, Beats 79.3%
    # 25.9 MB, Beats 96.56%
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for i in nums:
            if i in table:
                return True
            else:
                table[i] = i
        return False

    # 578 ms, Beats 42.89%
    # 28.8 MB, Beats 47.79%
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

    # 706 ms, Beats 12.98%
    # 25.8 MB, Beats 96.56%
    def contains_Duplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
