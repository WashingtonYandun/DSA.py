# Summation of primes
'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


import math


def is_prime_improved(num):
    primeFlag = True
    if num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                primeFlag = False
                return primeFlag
    return primeFlag


def summation_of_primes(target):
    totalSum = 0
    for i in range(2, target + 1, 1):
        if is_prime_improved(i):
            totalSum = totalSum + i
    return totalSum


print(summation_of_primes(2000000))  # 142913828922
