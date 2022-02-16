# Largest prime factor
'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


import math


def is_prime(num):
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
    factors = []
    for i in range(1, int(math.sqrt(num)) + 2):
        if num % i == 0:
            factors.append(i)
    return factors


def largest_prime_factor(num):
    factors = get_factors(num)
    currentMax = 0
    for i in factors:
        if is_prime(i) and i > currentMax:
            currentMax = i
    return currentMax


print(largest_prime_factor(600851475143))  # 6857
