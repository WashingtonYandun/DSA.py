# 229. Majority Element II
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

class Solution:
    # 87 ms, Beats 99.98%
    # 18.56 MB, 17.49%
    def majorityElement(self, nums: List[int]) -> List[int]:
        majs = {}
        res = []
        n = len(nums)
        m = n//3
        
        for i in nums:
            if i in majs:
                majs[i] += 1
            else:
                majs[i] = 1

        for i in range(n):
            if majs[nums[i]] > m and nums[i] not in res:
                res.append(nums[i])

        return res