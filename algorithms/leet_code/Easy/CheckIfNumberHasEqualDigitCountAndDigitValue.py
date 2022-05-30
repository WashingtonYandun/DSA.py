# 2283. Check if Number Has Equal Digit Count and Digit Value
'''
You are given a 0-indexed string num of length n consisting of digits.
Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.
'''


class Solution:
    # 31 ms, faster than 75.00%
    # 13.8 MB, less than 75.00%
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True
