import math
import os
import random
import re
import sys


def sum_of_two(arr, value):
    """
    For each element in the array, check if the difference between the value and the element is in the
    array

    :param arr: an array of integers
    :param value: the value we're looking for
    :return: True or False
    """
    for i in arr:
        diff = value - i
        if diff in arr:
            return True
    return False


def sum_of_two_all(arr, value):
    """
    It loops through the array, and for each element, it loops through the array again, and if the sum
    of the two elements is equal to the value, it adds the pair to the dictionary

    :param arr: an array of integers
    :param value: the sum of the two numbers
    :return: A dictionary with the number of pairs and the pairs themselves.
    """
    cont = 0
    pairs = {"Pairs": cont}

    for i in range(0, len(arr)):
        j = i + 1
        for j in range(j, len(arr)):
            if (arr[i] + arr[j] == value):
                cont = cont + 1
                pairs[cont] = [arr[i], arr[j]]

    pairs["Pairs"] = cont
    return pairs


def fibo_rc(num):
    """
    If the number is 0, return 0. If the number is 1, return 1. Otherwise, return the sum of the
    previous two numbers

    :param num: The number of the Fibonacci sequence you want to find
    :return: the sum of the two previous numbers in the sequence.
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_rc(num - 1) + fibo_rc(num - 2)


def fibo_m(num, memory={0: 0, 1: 1, 2: 1, 3: 2}):
    """
    If the number is in the memory, return it. Otherwise, calculate the number and store it in the
    memory

    :param num: The number of the Fibonacci sequence you want to find
    :param memory: a dictionary that stores the values of the fibonacci sequence
    :return: The nth number in the Fibonacci sequence.
    """
    if num in memory:
        return memory[num]
    memory[num] = fibo_m(num - 1) + fibo_m(num - 2)
    return memory[num]


def fact_rc(num):
    """
    If the number is 0 or 1, return 1. Otherwise, return the number multiplied by the factorial of the
    number minus 1

    :param num: The number to calculate the factorial of
    :return: The factorial of the number.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num*fibo_rc(num - 1)


def fact_m(num, memory={0: 1, 1: 1, 2: 2}):
    """
    If the number is in the memory, return it. Otherwise, calculate the factorial and store it in the
    memory

    :param num: The number to calculate the factorial of
    :param memory: a dictionary that will store the results of the factorials that have already been
    calculated
    :return: The factorial of the number.
    """
    if num in memory:
        return memory[num]
    memory[num] = num*fact_m(num - 1)
    return memory[num]


def is_odd(n):
    # must be improved
    """
    If the number of divisors of a number is greater than 2, then it is not prime

    :param n: the number to be checked
    :return: True or False
    """
    flag = True
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
            if cont > 2:
                return False
    return flag


def is_even(n):
    """
    If n is even, return True, otherwise return False

    :param n: The number to check
    :return: True or False
    """
    if n % 2 == 0:
        return True
    return False


def partition(arr, k):
    """
    It takes an array and a number k, and returns an array of arrays, each of which is a subarray of the
    original array, and each of which has a length of k

    :param arr: the array to be partitioned
    :param k: the number of elements in each sublist
    :return: A list of lists.
    """
    subs = []
    for i in range(0, len(arr), k):
        s = [arr[i:i + k]]
        subs.append(s)
    return subs


digits = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'}
