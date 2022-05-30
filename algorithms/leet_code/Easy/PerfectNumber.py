# 507. Perfect Number
'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.
'''


class Solution:
    # 9734 ms, faster than 5.32%
    # 13.9 MB, less than 10.99%
    def checkPerfectNumber(self, num: int) -> bool:
        n = 0
        if num > 90000001:  # there are not many perfect numbers between 1 and 90000001
            return False

        for i in range(1, int(num**1/2)+1, 1):
            if num % i == 0:
                n = n + i

        if n == num:
            return True

        return False
