# 57. Insert Interval
'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
'''

class Solution:
    # 76ms, Beats 66.48%
    # 19.77MB, Beats 95.36%
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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