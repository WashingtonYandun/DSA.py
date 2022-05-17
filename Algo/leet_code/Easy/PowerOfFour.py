# 342. Power of Four
'''
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
'''

class Solution:
    # 54 ms, faster than 27.90% 
    # 13.9 MB, less than 9.38%
    def isPowerOfFour(self, n: int) -> bool:
        """
        Brute force algo for check if (n) is a power of 4

        :param n: int
        :return: If is a pwer of two or not: bool
        """
        power = 0
        current = 0
        
        while power < n:
            power = 4 ** current
            if power == n:
                return True
            
            current = current + 1
        
        return False