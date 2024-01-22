# 645. Set Mismatch
'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''

class Solution:
    # 1879ms, Beats 12.41%
    # 17.99MB, Beats 86.03%
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lost = []
        l = 0

        for i in nums:
            if i in lost:
                l = i
                break
            
            lost.append(i)


        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        m = expected - (actual - l)

        return [l, m]