# 1360. Number of Days Between Two Dates
'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
'''

from datetime import datetime

class Solution:
    # 37ms, Beats 70.52%
    # 17.51MB, Beats 6.33%
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date2, "%Y-%m-%d") - datetime.strptime(date1, "%Y-%m-%d")).days)