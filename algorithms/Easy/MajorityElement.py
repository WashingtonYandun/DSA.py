# 169. Majority Element
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
 
class Solution:
    # 134 ms, Beats 98.43%
    # 18.8 MB, Beats 19.01%
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]