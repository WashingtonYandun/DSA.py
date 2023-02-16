# 2180. Count Integers With Even Digit Sum
'''
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
The digit sum of a positive integer is the sum of all its digits.
'''

class Solution:
    # 50 ms, faster than 78.70% 
    # 13.9 MB, less than 53.87%
    def countEven(self, num: int) -> int:
        evens = 0
        for i in range(1, num+1, 1):
            i = str(i)
            currentTotal = 0
            for j in i:
                currentTotal = currentTotal + int(j)
            
            if currentTotal % 2 == 0:
                evens = evens + 1
                
        return evens