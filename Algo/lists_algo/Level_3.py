# remember lists starts with index == 0
# M = R E nxn


'''
###########################
Rotate a Matrix 90 degrees.
###########################
'''


def transpose(M):
    Mt = list(map(list, zip(*M)))
    return Mt


def reverse_rows(M):
    for i in M:
        i = i.reverse()
    return M


def rotate(M):
    Mt = transpose(M)
    Mr = reverse_rows(Mt)
    return Mr


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix", M)
print("Rotated Matrix", rotate(M))
