import math
import os
import random
import re
import sys


def sum_of_two(arr, value):
    '''
    return a boolean value if exist a pair with the given sum.
    '''
    for i in arr:
        diff = value - i
        if diff in arr:
            return True
    return False


def sum_of_two_all(arr, value):
    '''
    return a dict of all the matches of pairs with the sum given
    '''
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
    '''
    recursive fibonacci
    '''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_rc(num - 1) + fibo_rc(num - 2)


def fibo_m(num, memory={0: 0, 1: 1, 2: 1, 3: 2}):
    '''
    dynamic programming fibonacci
    '''
    if num in memory:
        return memory[num]
    memory[num] = fibo_m(num - 1) + fibo_m(num - 2)
    return memory[num]


def fact_rc(num):
    '''
    recursive factorial
    '''
    if num == 0 or num == 1:
        return 1
    else:
        return num*fibo_rc(num - 1)


def fact_m(num, memory={0: 1, 1: 1, 2: 2}):
    '''
    dynamic programming factorial
    '''
    if num in memory:
        return memory[num]
    memory[num] = num*fact_m(num - 1)
    return memory[num]


def is_odd(n):
    '''
    verify if anumber is odd or not
    '''
    flag = True
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
            if cont > 2:
                return False
    return flag


def is_even(n):
    '''
    verify if anumber is even or not
    '''
    if n % 2 == 0:
        return True
    return False


def partition(arr, k):
    '''
    return an array of sub arrays in a defined lenght
    '''
    subs = []
    for i in range(0, len(arr), k):
        s = [arr[i:i + k]]
        subs.append(s)
    return subs
