# 28. Find the Index of the First Occurrence in a String
'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    # 29ms, Beats 94.74%
    # 16.53MB, Beats 56.37%
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1