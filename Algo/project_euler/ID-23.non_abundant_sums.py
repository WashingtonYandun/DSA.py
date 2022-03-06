# Non-abundant sums
'''
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


from ast import Break


def divisors_sum(num):
    count = 0
    for i in range(1, num, 1):
        if num % i == 0:
            count = count + i
    return count


def get_abundants(limit):
    abundants = [i for i in range(12, limit + 1, 1) if divisors_sum(i) > i]
    return abundants


def non_abundant_sums(limit):
    totalSum = 0
    abundants = get_abundants(limit)
    for j in range(0, len(abundants)):
        for k in range(j + 1, len(abundants)):
            if j == abundants[j] + abundants[k]:
                pass
            else:
                totalSum = totalSum + j
                break
    return totalSum


print(non_abundant_sums(28123))
