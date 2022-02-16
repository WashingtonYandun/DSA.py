# Sum square difference
'''
Problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sum_square_difference(num):
    y = ((num * (num + 1))/2)**2
    x = 0
    for i in range(1, num + 1, 1):
        x = x + i**2
    return y - x


print(sum_square_difference(100))
