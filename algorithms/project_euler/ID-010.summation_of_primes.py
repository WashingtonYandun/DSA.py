# Summation of primes
'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


import math


def is_prime_improved(num):
    """
    If the number is even and greater than 2, it's not prime. Otherwise, check if it's divisible by any
    odd number between 3 and the square root of the number. If it is, it's not prime. Otherwise, it is
    prime
    
    :param num: The number to be checked for primality
    :return: a boolean value.
    """
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
    """
    For each number between 2 and the target number, if the number is prime, add it to the total sum
    
    :param target: the number we want to find the sum of all primes below
    :return: The sum of all prime numbers below the target number.
    """
    totalSum = 0
    for i in range(2, target + 1, 1):
        if is_prime_improved(i):
            totalSum = totalSum + i
    return totalSum


print(summation_of_primes(2000000))  # 142913828922
