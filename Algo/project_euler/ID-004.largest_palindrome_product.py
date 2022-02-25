# Largest palindrome product
'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


'''
###############################
This is not an optimal solution
###############################
'''


def is_palindrome(num):
    palindromeFlag = False
    strNum = str(num)
    if strNum == strNum[::-1]:
        palindromeFlag = True
        return palindromeFlag
    return palindromeFlag


def largest_palindrome_product(num):
    maxLimit = 10 ** num - 1  # 3 - 999
    minLimit = maxLimit//10 + 1  # 999 - 100

    currentProd = 0
    currentMax = 0

    for i in range(maxLimit, minLimit, -1):
        for j in range(i, minLimit, -1):
            currentProd = i * j
            if currentProd > currentMax and is_palindrome(currentProd):
                currentMax = currentProd
                break
    return currentMax


print(largest_palindrome_product(3))  # 906609
