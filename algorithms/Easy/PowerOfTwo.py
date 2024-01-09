# 231. Power of Two
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    # 50 ms, faster than 36.05%
    # 13.7 MB, less than 95.83%
    def isPowerOfTwo(self, n: int) -> bool:
        """
        All powers of two has only one "1" in the first char of its representation in binary.

        :param n: int
        :return: If is a pwer of two or not: bool
        """
        if n == 0:
            return False
        
        binNum = list(str(bin(n)))
        binNum.pop(0)
        binNum.pop(0)
        binNum.pop(0)
        
        if '1' in binNum:
            return False
        else:
            return True