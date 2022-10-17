# Factorial digit sum
'''
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def fact_rc(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact_rc(num - 1)


def factorial_digit_sum(num):
    arrF = list(str(fact_rc(num)))
    arrF = [int(i) for i in arrF]
    return sum(arrF)


print(factorial_digit_sum(100))  # 648
