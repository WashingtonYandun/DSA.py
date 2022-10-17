# Number letter counts
'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

unics = {
    0: "zero",  # thi is not necesary
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "seventeen",
    17: "eighteen",
    18: "sixteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand"
}
comps = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def dec(num):
    # // this helps to get the first element
    # % this helps to get the second
    name = comps[num//10] + "" + unics[num % 10]
    unics[num] = name
    return len(unics[num])


def hundreds(num):
    # multiples of 100 // this get the first element
    name = unics[num // 100] + "hundred"
    unics[num] = name
    return len(unics[num])


def hundreds_comp(num):
    name_len(int(str(num)[1:]))
    name = unics[num // 100] + "hundred" + "and" + unics[int(str(num)[1:])]
    unics[num] = name
    return len(unics[num])


def name_len(num):
    if num in unics:
        count = len(unics[num])
        return count
    else:
        if 20 < num < 100:
            return dec(num)
        elif 100 <= num <= 900 and num % 100 == 0:
            return hundreds(num)
        elif 100 <= num <= 999:
            return hundreds_comp(num)
        else:
            return None  # TODO: better handling errors


def number_letter_counts(num):
    count = 0
    for i in range(1, num + 1, 1):
        count = count + name_len(i)
    return count


# print(name_len(342)) # 23
# print(name_len(115)) # 20
print(number_letter_counts(1000))  # 21124
