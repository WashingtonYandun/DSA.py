# 744. Find Smallest Letter Greater Than Target
'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
'''

class Solution:
    # 106ms, Beats 94.53%
    # 17.51MB, Beats 6.07%
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n - 1

        while l <= r:
            m = l + (r - l) // 2

            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1
        
        return letters[l % n]