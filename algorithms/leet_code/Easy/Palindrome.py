# Palindrome

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


def isPalindrome(self, x: int) -> bool:
    """
    We convert the integer to a string, then reverse the string, and then compare the reversed string to
    the original string
    
    :param x: int
    :type x: int
    :return: True or False
    """
    x = str(x)
    y = x[::-1]
    if x == y:
        return True
    return False
