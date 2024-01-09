# 66. Plus One
'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''


class Solution:
    # 36 ms, faster than 79.69%
    # 13.8 MB, less than 59.81%
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        We convert the list of digits to a string, convert the string to an integer, add 1 to the integer,
        convert the integer back to a string, and then convert the string back to a list of digits
        
        :param digits: List[int]
        :type digits: List[int]
        :return: A list of integers
        """
        digits = [str(x) for x in digits]
        num = int("".join(digits))
        num = num + 1
        num = str(num)
        return list(num)
