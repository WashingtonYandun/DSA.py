# 125. Valid Palindrome
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''


class Solution:
    # 45 ms, faster than 90.62%
    # 14.9 MB, less than 32.61%
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        for i in range(0, len(s)):
            if s[i] in "!@$%^&*()_-+=?\"\'#/\{}[]>'<.,`~:; ":
                s[i] = ""

        s = "".join(s)
        s = s.lower()
        return s == s[::-1]
