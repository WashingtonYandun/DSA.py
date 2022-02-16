# Smallest multiple
'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


import re


def is_divisible_to(num):
    multipleFlag = True
    for i in range(1, 20 + 1, 1):
        if num % i != 0:
            multipleFlag = False
            return multipleFlag
    return multipleFlag


def smallest_multiple():
    i = 20
    while(True):
        if is_divisible_to(i):
            break
        i = i + 20
    return i


print(smallest_multiple())
