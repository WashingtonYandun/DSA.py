class Solution:
    # 63 ms, faster than 19.64%
    # 13.8 MB, less than 74.74%
    def rotate(self, matrix: List[List[int]]) -> None:
        # REVERSE THEN TRANSPOSE
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]


'''
#############################
&&&&&  MY OLD SOLUTIONS &&&&&
#############################
'''

# remember lists starts with index == 0
# M = R E nxn


'''
###########################
Rotate a Matrix 90 degrees.
###########################
'''


def transpose(M):
    """
    It takes a matrix M as input and returns the transpose of M as output

    :param M: the matrix to be transposed
    :return: The transpose of the matrix M.
    """
    Mt = list(map(list, zip(*M)))
    return Mt


def reverse_rows(M):
    """
    It reverse the rows of a matrix

    :param M: a list of lists
    :return: the original matrix.
    """
    for i in M:
        i = i.reverse()
    return M


def rotate(M):
    """
    Rotate a Matrix 90 degrees.
    We transpose the matrix, then reverse the rows of the transposed matrix

    :param M: a matrix
    :return: The transpose of the matrix, with the rows reversed.
    """
    # TRANSPOSE THEN REVERSE BUT MODIFYING
    Mt = transpose(M)
    Mr = reverse_rows(Mt)
    return Mr