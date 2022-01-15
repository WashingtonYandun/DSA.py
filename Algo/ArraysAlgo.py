import time  # messuarte the execution time
import sys  # for increment the recursion limit


def sum_of_two(arr, value):
    '''
    In a given list if there is a pair of element that matches the sum given, return true.
    '''
    for i in arr:
        diff = value - i
        if diff in arr:
            return True
    return False


def sum_of_two_all(arr, value):
    '''
    Print all the matches of the sum_of_two problem. return true if it exist
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
