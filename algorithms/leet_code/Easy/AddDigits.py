# 258. Add Digits
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''


class Solution:
    # 42 ms, faster than 60.83%
    # 13.7 MB, less than 99.82%
    def addDigits(self, num: int) -> int:

        if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            return num

        while num not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            num = sum(int(i) for i in str(num))
            if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                return num

        return 0
