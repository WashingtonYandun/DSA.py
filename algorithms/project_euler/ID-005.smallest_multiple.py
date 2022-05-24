# Smallest multiple
'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def is_divisible_to(num, div):
    """
    It returns True if the number is divisible by all numbers from 1 to div, otherwise it returns False.
    
    :param num: The number to check if it's divisible to the div parameter
    :param div: the number to divide by
    :return: True or False
    """
    multipleFlag = True
    for i in range(1, div + 1, 1):
        if num % i != 0:
            multipleFlag = False
            return multipleFlag
    return multipleFlag


def smallest_multiple():
    """
    It starts with the number 20, and then keeps adding 20 to it until it finds a number that is
    divisible by all the numbers from 1 to 20
    :return: The smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
    """
    i = 20
    while(True):
        if is_divisible_to(i, 20):
            break
        i = i + 20
    return i


print(smallest_multiple())
