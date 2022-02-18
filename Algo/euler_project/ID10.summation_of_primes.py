# Summation of primes
'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


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


def st_prime(target):
    totalSum = 2
    for i in range(3, target + 1, 2):
        if is_prime(i):
            totalSum = totalSum + i
    return totalSum


print(st_prime(2000000))
