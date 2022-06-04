# 766. Toeplitz Matrix
'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''


class Solution:
    # 91 ms, faster than 84.25%
    # 13.8 MB, less than 79.11%
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):

                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True
