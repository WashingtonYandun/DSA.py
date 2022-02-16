# Multiples of 3 or 5
'''
Show HTML problem content 
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiples_of_three_or_five(num):
    totalSum = 0
    for i in range(1, num, 1):
        if i % 3 == 0 or i % 5 == 0:
            totalSum = totalSum + i
    return totalSum


print(multiples_of_three_or_five(1000))  # 23
