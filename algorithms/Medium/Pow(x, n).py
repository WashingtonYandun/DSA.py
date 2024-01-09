# 50. Pow(x, n)
'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
            power = 1
            oldN = n
            n = abs(n)

            for i in range(1,n+1):
                power = power * x

            if oldN > 0:
                return power
            else:
                return 1/power
            '''
        # tricky xd
        return x ** n
