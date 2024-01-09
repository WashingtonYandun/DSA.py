# 70. Climbing Stairs
'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    # 32 ms, Beats 64.14%
    # 14.1 MB, Beats 94.64%
    def climbStairs(self, n: int) -> int:
        arr = [0, 1]
        cont = 0
        for i in range(n):
            cont = arr[-1] + arr[-2]
            arr.append(cont)
        return cont
