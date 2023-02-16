# 1137. N-th Tribonacci Number

'''
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

# from functools import lru_cache
@lru_cache(None)
'''


class Solution:
    def tribonacci(self, n: int, memory={0: 1, 1: 1, 2: 1, 3: 2, 4: 4}) -> int:
        """
        We use a dictionary to store the values of the tribonacci sequence, and if the value is not in the
        dictionary, we calculate it and store it in the dictionary
        
        :param n: the nth number in the tribonacci sequence
        :type n: int
        :param memory: a dictionary that stores the values of the tribonacci sequence
        :return: The nth number in the tribonacci sequence.
        """
        if n in memory:
            return memory[n]
        memory[n] = self.tribonacci(
            n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return memory[n]


# ob = Solution()
# print(ob.tribonacci(1000))
