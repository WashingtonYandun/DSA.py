# 989. Add to Array-Form of Integer
'''
The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''


class Solution:
    # 323 ms, faster than 74.79%
    # 15.1 MB, less than 53.51%
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(x) for x in num]
        n = int("".join(num))
        n = str(n + k)
        return list(n)
