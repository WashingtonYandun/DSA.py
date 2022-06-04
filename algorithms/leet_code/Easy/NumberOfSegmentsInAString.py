# 434. Number of Segments in a String
'''
Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.
'''


class Solution:
    # 24 ms, faster than 98.01%
    # 14 MB, less than 6.96%
    def countSegments(self, s: str) -> int:
        l = len(s.strip().split())
        return l
