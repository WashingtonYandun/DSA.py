# Weird Algorithm
'''
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a given value of n.
'''


def weird(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        print(n)


weird(3)
