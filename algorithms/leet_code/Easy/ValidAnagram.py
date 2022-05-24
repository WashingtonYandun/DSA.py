# 242. Valid Anagram
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution:
    # 50 ms, faster than 85.42%
    # 15.5 MB, less than 11.68%
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        s = sorted(s)
        t = sorted(t)

        if len(s) == len(t):
            if s == t:
                return True

        return False
