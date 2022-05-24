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
    Mt = transpose(M)
    Mr = reverse_rows(Mt)
    return Mr


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix", M)
print("Rotated Matrix", rotate(M))
