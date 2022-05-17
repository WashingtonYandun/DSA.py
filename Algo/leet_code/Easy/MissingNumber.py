# 268. Missing Number
'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''


class Solution:
    # 156 ms, faster than 69.89%
    # 15.4 MB, less than 16.72%
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        myList = []
        
        for i in range(0, n+1):
            myList.append(i)
            
        return sum(myList) - sum(nums)

    
    # 136 ms, faster than 91.50%
    # 15.1 MB, less than 77.79%
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        real = n*(n+1)/2
        return int(real - sum(nums))