# Sqrt(x)
'''
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''


class Solution:
    # 48 ms, faster than 64.71%
    # 13.9 MB, less than 57.44%
    def mySqrt(self, x: int) -> int:
        """
        We are using the Newton's method to find the square root of a number

        :param x: int -> The number we want to find the square root of
        :type x: int
        :return: The square root of the number
        """
        # return int(x ** 0.5) -> Tricky one xd
        result = 1
        for i in range(30):
            result = 1/2 * (result + x/result)
        return int(result)
