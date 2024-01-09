# 15. 3Sum
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''


class Solution:
    
    # 1103ms Beats 85.53%of users with Python3
    # 20.45mb Beats 67.98%of users with Python3

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to pointers aproach
        result = []

        for i in range(len(nums) - 2):
            # skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_sum < 0:
                    left += 1
                    
                else:
                    right -= 1

        return result
