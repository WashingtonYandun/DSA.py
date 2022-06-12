# 263. Ugly Number
'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
'''


class Solution:
    # 60 ms, faster than 19.62%
    # 13.8 MB, less than 96.52%
    def isUgly(self, n: int) -> bool:

        if n < 0 or n == 0:
            return False

        while n > 6:
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
        return True
