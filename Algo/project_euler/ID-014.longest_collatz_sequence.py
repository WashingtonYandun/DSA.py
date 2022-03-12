# Longest Collatz sequence
'''
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


'''
#################################
FIRST IMPLEMENTATION OF COLLATZ
#################################
'''

'''
memory = {}
def collatz(num):
    # TODO: USE THIS IMPROVE THE PROGRAM
    count = 0
    if not num in memory:
        if num == 1:
            memory[num] = 1
        elif num % 2 == 0:
            memory[num] = collatz(num // 2)
        else:
            memory[num] = collatz(3 * num + 1)
    return memory[num]


print(collatz(9), memory)
# i dind't know how to continue with this function
'''


def collatz_sq(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        count += 1
    return count


def longest_collatz_sequence(r):
    currentMax = 1
    currentNum = 1
    for i in range(r, 1, -1):
        count = collatz_sq(i)
        if count > currentMax:
            currentMax = count
            currentNum = i
    return [currentNum, currentMax]


print(longest_collatz_sequence(1_000_000))  # [837799, 525]
