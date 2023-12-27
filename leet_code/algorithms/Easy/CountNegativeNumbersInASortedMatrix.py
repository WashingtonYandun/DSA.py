# 1351. Count Negative Numbers in a Sorted Matrix
'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''

class Solution:
    # 94ms, Beats 99.92%
    # 18.29MB, Beats 7.81%
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in grid:
            l = 0
            r = len(i) - 1

            while l <= r:
                m = l + (r - l) // 2

                if i[m] < 0:
                    count += r - m + 1
                    r = m - 1
                else:
                    l = m + 1

        return count


class SolutionWithBinarySearch:
    # 95ms, Beats 99.85%
    # 18.24MB, Beats 7.81%
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in grid:
            n = len(i)
            for j in range(0, n):
                if i[j] < 0:
                    count += n - j
                    break
        
        return count