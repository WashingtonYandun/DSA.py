import math
import os
import random
import re
import sys

# trd == traditional
# ps == python style or using python tricks
# tle == Time Limit Exceeded
# mt == math solution

'''
**************** Cyclically rotate an array by one ****************
Given an array, rotate the array by one position in clock-wise direction.
'''


def rotate(arr):
    """
    It takes an array, removes the last element, and adds it to the front of the array
    
    :param arr: The array to rotate
    :return: The last element of the array is being returned.
    """
    arrN = [arr[-1]]
    arr.pop()
    return arrN + arr


def rotate_ps(arr):
    """
    It rotates the array to the right by one position.
    
    :param arr: the array to be rotated
    :return: The last element of the array is being returned.
    """
    arr[:] = arr[-1::] + arr[::-1]
    return arr


'''
**************** Missing number in array ****************
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.
'''


def missing_number_mt(arr, n):
    """
    We know that the sum of the first n natural numbers is n(n+1)/2. So, we can find the missing number
    by subtracting the sum of the array from the sum of the first n natural numbers
    
    :param arr: an array of integers
    :param n: the length of the array
    :return: The missing number in the array
    """
    n = len(arr)+1
    s = n*(n + 1)/2
    cs = sum(arr)
    return int(s - cs)


'''
**************** Count pairs with given sum ****************
Given an array of N integers, and an integer K,
find the number of pairs of elements in the array whose sum is equal to K.
'''


def get_pairs_count_tle(arr, k):
    """
    For each element in the array, check every other element in the array to see if they sum to k
    
    :param arr: an array of integers
    :param k: the number we're looking for
    :return: The number of pairs of elements in the array that sum to k.
    """
    cont = 0
    for i in range(0, len(arr)):
        j = i + 1
        for j in range(j, len(arr)):
            if (arr[i] + arr[j] == k):
                cont = cont + 1
    return cont


'''
**************** Quick Sort ****************
Quick Sort is a Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position low and its ending position high.

Implement the partition() and quickSort() functions to sort the array.
'''


def quick_sort(arr):
    """
    If the array is empty or has one element, return it. Otherwise, take the last element as the pivot,
    remove it from the array, and put all the elements smaller than the pivot in a new array, and all
    the elements larger than the pivot in another new array. Then, return the result of calling
    quick_sort on the smaller array, followed by the pivot, followed by the result of calling quick_sort
    on the larger array
    
    :param arr: the array to be sorted
    :return: the sorted array.
    """
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[-1]
    arr.pop()

    lowers = []
    highers = []

    for i in arr:
        if i > pivot:
            highers.append(i)
        else:
            lowers.append(i)

    return quick_sort(lowers) + [pivot] + quick_sort(highers)


'''
**************** Common elements ****************
Given three arrays sorted in increasing order.
Find the elements that are common in all three arrays.
'''


def common_elements_tle(A, B, C):
    """
    Intersecction of 3 arrays
    For each element in A, check if it is in A, B, and C. If it is, add it to the set of common elements
    
    :param A: list of integers
    :param B: list of integers
    :param C: list of integers
    :return: A list of the common elements in A, B, and C.
    """
    commons = set()
    for i in A:
        if (i in A and i in B and i in C):
            commons.add(i)
    commons = list(commons)
    commons = sorted(commons)
    return commons


# Return to make this better
def common_elements_tle2(A, B, C):
    """
    Intersecction of 3 arrays
    For each element in A, check if it is in A, B, and C. If it is, add it to the set of common elements
    
    :param A: list of integers
    :param B: list of integers
    :param C: list of integers
    :return: A list of the common elements in A, B, and C.
    """
    commons = []
    for i in A:
        if (i in A and i in B and i in C and i not in commons):
            commons.append(i)
    return commons


'''
**************** First Repeating Element ****************
Given an array arr[] of size n, find the first repeating element.
The element should occurs more than once and the index of its first occurrence should be the smallest.
'''


def first_repeated(arr):
    """
    The first element that is repeated
    
    :param arr: The array to search through
    :return: The first repeated element in the array.
    """
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return -1


'''
**************** Binary Search ****************
Given an array arr[] of size n, find the first repeating element.
The element should occurs more than once and the index of its first occurrence should be the smallest.
'''


def binary_search(arr, value):
    """
    If the value is not in the array, return None. If the value is in the array, return True
    
    :param arr: The array to search through
    :param value: the value you're looking for
    :return: True or None
    """
    if value not in arr:
        return None

    nArr = []

    n = len(arr)
    pivot = arr[(n//2)]

    if pivot == value:
        return True

    if value > pivot:
        nArr = arr[pivot:]
    else:
        nArr = arr[0:pivot-1]

    return binary_search(nArr, value)


def binary_search(arr, value):
    #must be improved
    i = 0
    return arr[i]
