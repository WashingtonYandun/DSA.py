# 7. Reverse Integer
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    # Need and improvement in validation

    # 47 ms, faster than 37.41%
    # 16.3 MB, less than 35.15%
    def reverse(self, x: int) -> int:
        strNum = str(x)
        sign = ""
        if(strNum[0] in "+-"):
            strNum = list(strNum)
            sign = strNum[0]
            strNum.pop(0)
            strNum = "".join(strNum)

        strNum = strNum[::-1]
        result = int(sign + strNum)

        if result < (-2**31) or result > (2**31) -1:
            return 0
        return int(result)