# 8. String to Integer (atoi)

# I really hate this problem. It's not hard, but it's just so annoying to deal with all the edge cases.

'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
'''

class Solution:
    # 31 ms, Beats 96.08%
    # 17.28 MB, Beats 37.62%
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        # Check for sign
        if not s:
            return 0
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
            
        # Read digits until the next non-digit character
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        
        # Apply sign and handle 32-bit integer range
        result = sign * num
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result