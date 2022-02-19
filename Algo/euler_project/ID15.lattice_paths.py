# Lattice paths
'''
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''


def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)


def lattice_paths(gridDim):
    numPaths = fact(2*gridDim)/fact(gridDim)**2
    return int(numPaths)


print(lattice_paths(20))
