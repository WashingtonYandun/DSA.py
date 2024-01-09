# 415. Add Strings
'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''


class Solution:
    # 42 ms, faster than 85.33%
    # 14 MB, less than 67.07%
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))
