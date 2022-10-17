# Counting Sundays
'''
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


# implementating Zeller's congruence
# For the Gregorian calendar, Zeller's congruence is:


import math

'''
def is_leap(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
    elif y % 4 == 0:
        return True
    return False
'''


def zeller_cong(d, m, y):
    '''
    @return h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
    '''
    h = -1
    q = d
    # input m will be the index of m-arr
    months = [0, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    k = y % 100
    j = y//100
    h = (q + math.floor(13*(months[m]+1)/5) + k +
         math.floor(k/4) + math.floor(j/4) - (2*j)) % 7
    return h


def counting_sundays(start, last):
    count = 0
    for y in range(start, last + 1, 1):
        for m in range(1, 13, 1):
            if zeller_cong(1, m, y) == 1:
                count = count + 1
    return count


print(counting_sundays(1901, 2000))  # 171
# maybe there is some errors but there is the answer
