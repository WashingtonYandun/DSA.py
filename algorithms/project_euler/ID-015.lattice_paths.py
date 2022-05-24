# Lattice paths
'''
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''


def fact(num):
    """
    It takes a number and returns the factorial of that number
    
    :param num: the number to calculate the factorial of
    :return: The factorial of the number.
    """
    # TODO: need improve factorial function
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)


def lattice_paths(gridDim):
    """
    The number of lattice paths from the origin to a point $(x,y)$ is equal to the number of lattice
    paths from the origin to $(x-1,y)$ plus the number of lattice paths from the origin to $(x,y-1)$
    
    :param gridDim: The dimension of the grid. For example, a 2x2 grid has gridDim = 2
    :return: The number of paths from the top left corner to the bottom right corner of a grid of size
    gridDim x gridDim.
    """
    numPaths = fact(2*gridDim)/fact(gridDim)**2
    return int(numPaths)


print(lattice_paths(20))  # 137846528820
