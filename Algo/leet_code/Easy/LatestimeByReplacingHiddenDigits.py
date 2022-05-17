# 1736. Latest Time by Replacing Hidden Digits
'''
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.
'''


class Solution:
    # 29 ms, faster than 89.47%
    # 13.9 MB, less than 71.23%
    def maximumTime(self, time: str) -> str:
        time = [list(x) for x in time.split(":")]

        if "?" in time[0]:
            if time[0][0] in "01":
                time[0][1] = "9"
            elif time[0][0] in "2":
                time[0][1] = "3"
            elif time[0][1] in "0123":
                time[0][0] = "2"
            elif time[0][1] in "456789":
                time[0][0] = "1"
            elif time[0][0] == "?" and time[0][1] == "?":
                time[0][0] = "2"
                time[0][1] = "3"

        if "?" in time[1]:
            if time[1][0] in "0123456":
                time[1][1] = "9"
            elif time[1][1] in "012345689":
                time[1][0] = "5"
            elif time[1][0] == "?" and time[1][1] == "?":
                time[1][0] = "5"
                time[1][1] = "9"


        newHour = "".join(time[0])
        newMin = "".join(time[1])
        
        return f"{newHour}:{newMin}"