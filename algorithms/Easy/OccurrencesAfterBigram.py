# 1078. Occurrences After Bigram
'''
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".
'''

class Solution:
    # 32ms, Beats 88.16%
    # 17.26MB, Beats 8.93%
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = text.split()
        n = len(s) - 2
        res = []
        for i in range(n):
            if s[i] == first and s[i+1] == second:
                res.append(s[i+2])

        return res
