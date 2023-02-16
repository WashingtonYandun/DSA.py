# Roman To int

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        We iterate through the string, and if the current character and the next character form a key in
        our dictionary, we add the corresponding value to our total. Otherwise, we just add the value of
        the current character.
        
        :param s: str
        :type s: str
        :return: The number of the roman numeral
        """
        n = len(s)
        romanNums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            # add special numbers for making easier
            # these are for i = i + 2 numbers
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        i = 0
        num = 0
        while i < n:
            if i+1 < n and s[i:i+2] in romanNums:
                # for special numbers like 4s and 9s
                num = num + romanNums[s[i:i+2]]
                i = i + 2
            else:
                # for simple numbers
                num = num + romanNums[s[i]]
                i = i + 1
        return num


# ob = Solution()
# print(ob.romanToInt("MCMXCIV"))
