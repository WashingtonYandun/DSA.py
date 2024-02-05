# 1967. Number of Strings That Appear as Substrings in Word
'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    # 38ms, Beats 79.86%
    # 16.65MB, Beats 54.86%
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        for i in patterns:
            if i in word:
                c += 1

        return c