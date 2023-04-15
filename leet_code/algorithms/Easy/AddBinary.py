# 67. Add Binary
'''
Given two binary strings a and b, return their sum as a binary string.
'''


class Solution:
    # 28 ms, faster than 97.46%
    # 13.8 MB, less than 73.53%
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]  # first two chars are 0b
