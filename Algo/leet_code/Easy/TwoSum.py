# Two Sum

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


class Solution:
    def twoSumN2(nums, target):
        """
        For each element in the list, check if there is another element that sums to the target
        
        :param nums: the list of numbers
        :param target: the sum we're looking for
        :return: The indices of the two numbers that add up to the target.
        """
        n = len(nums)
        for i in range(0, n):
            j = i + 1
            for j in range(j, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]


def twoSumN(nums, target):
    """
    For each number in the list, we check if the difference between the target and the current number is
    in the dictionary. If it is, we return the difference and the current number. If it isn't, we add
    the current number to the dictionary
    
    :param nums: the list of numbers
    :param target: the target sum
    """
    differences = {}
    n = len(nums)
    for i in range(0, n):
        currentNum = nums[i]
        if differences[target - currentNum]:
            return differences[target - currentNum]
        differences[currentNum] = [target - currentNum, [i]]


n = [1, 2, 3, 4, 5, 9, 10, 20, 19]
print(twoSumN(n, 20))
