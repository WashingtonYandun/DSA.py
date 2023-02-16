# 728. Self Dividing Numbers
'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
'''


class Solution:
    # 78 ms, faster than 37.88%
    # 13.9 MB, less than 73.32%
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            strNum = str(i)
            if "0" not in strNum:
                for j in strNum:
                    flag = True
                    if i % int(j) != 0:
                        flag = False
                        break
                if flag:
                    result.append(i)
        return result
