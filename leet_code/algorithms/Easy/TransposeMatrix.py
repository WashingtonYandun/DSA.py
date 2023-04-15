# 867. Transpose Matrix
'''
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''


class Solution:
    # 88 ms, faster than 62.25%
    # 14.7 MB, less than 55.33%
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_transposed = list(map(list, zip(*matrix)))
        return matrix_transposed