# 405. Convert a Number to Hexadecimal
'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
'''


class Solution:
    # 30 ms, beats 93.01%
    # 17.27 MB, beats 16.90%
    def toHex(self, num: int) -> str:
        hex_chars = "0123456789abcdef"
        result = ""

        if num == 0:
            return "0"

        # Convert negative to 32-bit two's complement
        if num < 0:
            num += 2 ** 32

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num //= 16

        return result