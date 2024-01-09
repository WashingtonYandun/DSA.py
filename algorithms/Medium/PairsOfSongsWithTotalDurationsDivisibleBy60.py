# 1010. Pairs of Songs With Total Durations Divisible by 60
'''
You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
'''

class Solution:
    # 220ms, Beats 99.29%
    # 21.92MB, Beats 5.17%
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem  = [0] * 60
        res = 0
        
        for t in time:
            r = t % 60
            c = (60 - r) % 60

            res += rem[c]
            rem[r] += 1
        
        return res