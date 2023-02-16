# 43. Permutations
'''
Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.
'''

from itertools import permutations


class Solution:

    # 44 ms, faster than 80.40%
    # 13.9 MB, less than 84.88%

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Using iteratools
        :param nums: List[int]
        :type nums: List[int]
        :return: A list of lists
        """
        perm = permutations(nums)

        result = []

        for i in perm:
            i = list(i)
            result.append(i)

        return result
