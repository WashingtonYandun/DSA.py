# 326. Power Of Three
'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

class Solution:
    # 169 ms, faster than 17.66%
    # 14 MB, less than 17.36%
    def isPowerOfThree(self, n: int) -> bool:
        """
        Brute force algo for check if (n) is a power of 3

        :param n: int
        :return: If is a pwer of two or not: bool
        """
        power = 0
        current = 0
        
        while power < n:
            power = 3 ** current
            if power == n:
                return True
            
            current = current + 1
        
        return False