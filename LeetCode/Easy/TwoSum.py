# Two Sum

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


class Solution:
    def twoSum(nums, target):
        '''
        return a pair with that mathces the given sum
        '''
        n = len(nums)
        for i in range(0, n):
            j = i + 1
            for j in range(j, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]
