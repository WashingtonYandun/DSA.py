# 58. Length of Last Word
'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    # 45 ms, faster than 39.46%
    # 14.1 MB, less than 5.60%
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")
        return len(s[-1])