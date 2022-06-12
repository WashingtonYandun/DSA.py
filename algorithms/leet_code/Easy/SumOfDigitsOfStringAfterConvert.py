# 1945. Sum of Digits of String After Convert
'''
You are given a string s consisting of lowercase English letters, and an integer k.
First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
'''


class Solution:
    # 50 ms, faster than 50.39%
    # 13.7 MB, less than 100.00% (wow)
    def getLucky(self, s: str, k: int) -> int:
        s = s.upper()
        num = [str(ord(i)-64) for i in s]
        num = "".join(num)

        for i in range(0, k):
            total = sum(int(i) for i in num)
            num = str(total)

        return total
