# 153. Find Minimum in Rotated Sorted Array
'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    # 45ms, Beats 69.23%
    # 17.52MB, Beats 10.20%
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1

        # The loop ends when l == r, pointing to the index with the minimum value
        while l < r:
            m = l + (r - l)//2

            # Compare nums[m] with nums[r] to determine which half to search
            if nums[m] <= nums[r]:
                # If nums[m] is less than or equal to nums[r], search in the left half
                r = m
            else:
                # If nums[m] is greater than nums[r], search in the right half
                l = m + 1
        
        return nums[r]
