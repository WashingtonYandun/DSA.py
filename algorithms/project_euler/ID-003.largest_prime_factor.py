# Largest prime factor
'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


import math


def is_prime(num):
    #must be improved
    """
    Takes a number as an argument and returns True if the number is prime and
    False if the number is not prime
    
    :param num: the number to be checked
    :return: the value of the variable primeFlag.
    """
    primeFlag = True
    count = 0
    for i in range(1, num + 1, 1):
        if num % i == 0:
            count = count + 1
            if count > 2:
                primeFlag = False
                return primeFlag
    return primeFlag


def get_factors(num):
    """
    It takes a number and returns a list of all the factors of that number
    
    :param num: The number to find the factors of
    :return: A list of factors of the number.
    """
    factors = []
    for i in range(1, int(math.sqrt(num)) + 2):
        if num % i == 0:
            factors.append(i)
    return factors


def largest_prime_factor(num):
    """
    It gets all the factors of the number, then checks if each factor is prime, and if it is, it checks
    if it's the largest prime factor so far
    
    :param num: The number to find the largest prime factor of
    :return: The largest prime factor of the number 600851475143
    """
    factors = get_factors(num)
    currentMax = 0
    for i in factors:
        if is_prime(i) and i > currentMax:
            currentMax = i
    return currentMax


print(largest_prime_factor(600851475143))  # 6857
