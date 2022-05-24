# 77. Combinations
'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.
'''

from itertools import *


class Solution:
    # 107 ms, faster than 89.72%
    # 15.9 MB, less than 85.33%
    def combine(self, n, k):
        """
        Using iteratools
        :param n: the number of elements in the set
        :param k: the number of elements in each combination
        :return: A list of lists of all possible combinations of k numbers from 1 to n.
        """
        perm = combinations([x for x in range(1, n+1)], k)
        result = []
        for i in perm:
            i = list(i)
            result.append(i)
        return result
