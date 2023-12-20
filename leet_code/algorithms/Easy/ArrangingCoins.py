# 441. Arranging Coins
'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
'''

class Solution:
    # 400ms Beats 44.71%
    # 17.27 MB beats 15.24%
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return n

        row = 1
        while(n >= row):
            n -= row
            row += 1
        
        return row - 1
