# 18. 4Sum
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''


class Solution:

    # 724ms Beats 74.72%of users with Python3
    # 16.36mb Beats 71.71%of users with Python3

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort() # two pointers aproach
        result = []

        for a in range(n - 3):
            # skip duplicates
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                # skip duplicates
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                # two pointers aproach
                left = b + 1
                right = n - 1

                while left < right:

                    current_sum = nums[a] + nums[b] + (nums[left] + nums[right])

                    if current_sum == target:
                        result.append([nums[a], nums[b], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < target:
                        left += 1
                        
                    else:
                        right -= 1

        return result
