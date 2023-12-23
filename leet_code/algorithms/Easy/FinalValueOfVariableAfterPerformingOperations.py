# 2011. Final Value of Variable After Performing Operations
'''
There is a programming language with only four operations and one variable X:
++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.
Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
'''

class Solution:
    # 48ms Beats 97.53%
    # 17.26MB Beats 29.32%
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for i in operations:
            if i[1] == "-":
                total -= 1
            else:
                total += 1
        return total