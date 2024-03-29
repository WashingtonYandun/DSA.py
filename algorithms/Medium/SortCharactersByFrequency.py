# 451. Sort Characters By Frequency
'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
'''

class Solution:
    # 35ms, Beats 98.63%
    # 18.71MB, Beats 25.39%
    def frequencySort(self, s: str) -> str:
        f = {}

        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        
        sor = dict(sorted(f.items(), key=lambda x: x[1], reverse=True))
        res = ''.join([k * v for k, v in sor.items()])
        return res