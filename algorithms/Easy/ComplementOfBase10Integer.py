# 1009. Complement of Base 10 Integer
'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
'''

class Solution:
    # 28ms, Beats 96.39%
    # 17.24MB, Beats 12.03%
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n)[2:].replace("1","x").replace("0", "1").replace("x", "0"), 2)