# 20. Valid Parentheses

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        """
        If the string is valid, then the stack should be empty at the end.
        
        :param s: str
        :type s: str
        :return: True or False
        """
        lefts = []

        for i in s:
            if i in ['(', '{', '[']:
                lefts.append(i)

            # check if a pair exists if all i has a pair
            # at the final lefts has to be empty
            elif i == ')' and len(lefts) != 0 and lefts[-1] == '(':
                lefts.pop()
            elif i == '}' and len(lefts) != 0 and lefts[-1] == '{':
                lefts.pop()
            elif i == ']' and len(lefts) != 0 and lefts[-1] == '[':
                lefts.pop()
            else:
                return False
        return len(lefts) == 0
