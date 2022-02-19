# Power digit sum
'''
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''


def power_digit_sum(a, p):
    r = a**p
    r = sum([int(i) for i in list(str(r))])
    return r


print(power_digit_sum(2, 1000))  # 1366
