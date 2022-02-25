# Amicable numbers
'''
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

'''
def euler_rule(n, m):
    if n > m > 0:
        p = ((2**(n - m) + 1) * 2**m) - 1
        q = ((2**(n - m) + 1) * 2**n) - 1
        r = (((2**(n - m) + 1)**2) * (2**(m + n))) - 1
        return [(2**n)*p*q, (2**n)*r]


print(euler_rule(2, 1))
'''


def divisors_sum(num):
    count = 0
    for i in range(1, num, 1):
        if num % i == 0:
            count = count + i
    return count


def is_amicable(numA):
    amicable = False
    numB = divisors_sum(numA)
    if numB != numA and divisors_sum(numB) == numA:
        amicable = True
        return amicable
    return amicable


def amicable_numbers(limit):
    total = 0
    for i in range(1, limit + 1, 1):
        if is_amicable(i):
            total = total + i
    return total


print(amicable_numbers(10_000))  # 31626
# this runs very slow obviously
