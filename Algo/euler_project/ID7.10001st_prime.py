# 10001st prime

'''
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


def st_prime(location):
    n = 13
    i = 5
    while(True):
        if is_prime(n):
            i = i + 1
            print(i, n)

        if i == location:
            return n

        n = n + 2


print(st_prime(10001))
