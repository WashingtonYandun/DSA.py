# 2108. Find First Palindromic String in the Array
'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
'''


class Solution:
    # 79 ms, faster than 80.25%
    # 13.9 MB, less than 70.35%
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i

        return ""
