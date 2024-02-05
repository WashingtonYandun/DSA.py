# 56. Merge Intervals
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    # 120ms, Beats 83.38%
    # 20.64MB, Beats 86.88%
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for i in intervals[1:]:
            # check overlap
            if i[0] > res[-1][1]:
                res.append(i)
            else:
                # update
                res[-1][1] = max(res[-1][1], i[1])

        return res