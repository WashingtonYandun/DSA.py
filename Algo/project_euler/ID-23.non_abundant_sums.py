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


def divisors_sum(num):
    count = 0
    for i in range(1, num, 1):
        if num % i == 0:
            count = count + i
    return count


def num_type(num):
    sumD = divisors_sum(num)
    if sumD > num:
        return 1
    elif sumD == num:
        return 0
    else:
        pass


def non_abundant_sums():
    limit = 28123
    total = 0
    perfects = []
    abundants = []

    for i in range(0, limit + 1):
        if num_type(i) == 1:
            abundants.append(i)
        elif num_type(i) == 0:
            perfects.append(i)

    for i in range(1, len(abundants)):
        for j in range(1, len(abundants)):
            current = abundants[i] + abundants[j]
            if current in perfects:
                total = total + current
            elif num_type(current) == 0:
                total = total + current
            else:
                pass
    return total


print(non_abundant_sums())


'''
TODO: SOLVE THIS
'''
