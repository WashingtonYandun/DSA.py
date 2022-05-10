import math
import os
import random
import re
import sys

# trd == traditional
# ps == python style or using python tricks
# tle == Time Limit Exceeded

''' 
**************** PEAK ELEMENT ****************
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.
'''


def peak_element_trd(arr):
    """
    If the current element is greater than the next element and the previous element, then return the
    current index
    
    :param arr: The array to search for a peak element in
    :return: The index of the peak element.
    """
    arr.append(0)
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            return i
    arr.pop()
    return None


def peak_element_ps(arr):
    """
    It returns the index of the maximum element in the array.
    
    :param arr: The array to be searched
    :return: The index of the maximum value in the array.
    """
    return arr.index(max(arr))


def peak_all_element(arr):
    """
    It takes an array, appends a zero to the end of it, then iterates through the array, checking if the
    current element is greater than the next and previous elements, and if so, appends the index of the
    current element to a list of peaks. Finally, it removes the zero from the end of the array and
    returns the list of peaks
    
    :param arr: The array to be searched
    :return: The index of the peak elements
    """
    arr.append(0)
    peaks = []
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            peaks.append(i)
    arr.pop()
    return peaks


''' 
**************** Find minimum and maximum element in an array ****************
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
'''


def get_min_max_trd(arr):
    """
    It loops through the array and compares each element to the current minimum and maximum values,
    updating them if necessary
    
    :param arr: the array to be searched
    :return: The minimum and maximum values of the array.
    """
    maximun = 0
    minimun = arr[0]
    for i in range(len(arr)):
        if arr[i] < minimun:
            minimun = arr[i]
        if arr[i] > maximun:
            maximun = arr[i]
    return minimun, maximun


def get_min_max_ps(arr):
    """
    It takes an array of numbers and returns the minimum and maximum values in the array
    
    :param arr: The array of numbers to be analyzed
    :return: The minimum and maximum values of the array.
    """
    return min(arr), max(arr)


''' 
**************** Reverse a String ****************
You are given a string s. You need to reverse the string.
'''


def reverse_word_trd(s):
    """
    It takes a string, s, and returns a string that is the reverse of s
    
    :param s: the string to be reversed
    :return: The reversed string
    """
    sReversed = ""
    for i in range(len(s)-1, -1, -1):
        sReversed = sReversed + s[i]
    return sReversed


def reverse_word_ps(s):
    """
    It takes a string, reverses it, and returns the reversed string
    
    :param s: The string to be reversed
    :return: The string s is being returned in reverse order.
    """
    return s[::-1]


''' 
**************** Sort The Array  ****************
Given a random set of numbers, Print them in sorted order.
'''


def bubble_sort(arr):
    """
    For each element in the array, compare it to the next element and swap them if the first element is
    greater than the second element
    
    :param arr: the array to sort
    :return: The sorted array
    """
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                # swap variables python style, we could use a temp var
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_list(arr):
    """
    It takes a list of numbers as an argument and returns a sorted list of those numbers
    
    :param arr: an array of integers
    :return: The sorted list
    """
    #must be done with more algos
    return sorted(arr)


''' 
**************** Kth smallest element ****************
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
'''


def kth_smallest(arr, k):
    """
    It sorts the array and returns the kth element
    
    :param arr: an array of integers
    :param k: the kth smallest element
    :return: The kth smallest element in the array.
    """
    # need an optimized solution
    return sorted(arr)[k-1]


''' 
**************** Find the Frequency ****************
Given a vector of N positive integers and an integer X.
The task is to find the frequency of X in vector.
'''


def find_frequency_ps(arr, x):
    """
    It iterates through the array and adds 1 to the xFrecuency variable every time it finds the number x
    
    :param arr: The array to search through
    :param x: The number you want to find the frequency of
    :return: The number of times that the number x appears in the array arr.
    """
    xFrecuency = 0
    for i in arr:
        if i == x:
            xFrecuency = xFrecuency + 1
    return xFrecuency


def find_frequency_trd(arr, x):
    """
    It iterates through the array and counts the number of times the value x appears in the array
    
    :param arr: The array to search in
    :param x: The number you want to find the frequency of
    :return: The number of times that the number x appears in the array.
    """
    xFrecuency = 0
    for i in range(0, len(arr)):
        if arr[i] == x:
            xFrecuency = xFrecuency + 1
    return xFrecuency


''' 
**************** Sort an array of 0s, 1s and 2s ****************
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
'''


def sort012(arr):
    """
    It sorts the array and returns the sorted array
    
    :param arr: an array of integers
    :return: None
    """
    arr = arr.sort()
    return arr


''' 
**************** Subarray with given sum ****************
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
'''


def sub_array_sum_tle(arr, s):
    """
    For each element in the array, we add it to the sum and check if the sum is equal to the given sum.
    If it is, we return the indices. If it is greater than the given sum, we break out of the loop. If
    it is less than the given sum, we keep adding the next element to the sum
    
    :param arr: The array to search through
    :param s: the sum we're looking for
    :return: The start and end index of the subarray that sums to the given sum.
    """
    for i in range(len(arr)):
        cs = arr[i]
        j = i + 1
        for j in range(i+1, len(arr)+1):
            if cs == s:
                return [i, j-1]

            if cs > s or j == len(arr):
                break
            cs = cs + arr[j]
    return [-1]


def sub_aray_sum(arr, n, s):
    """
    It starts with the first element of the array and keeps adding elements to the current sum until the
    current sum becomes equal to the sum s or it becomes greater than s. If the current sum becomes
    equal to s, then we return true and if the current sum becomes greater than s, then we remove
    trailing elements while the current sum is greater than s
    
    :param arr: The array to be searched
    :param n: length of the array
    :param s: the sum we're looking for
    :return: The start and end index of the subarray that sums to the given sum.
    """
    i = 0
    cs = arr[0]
    j = 1
    while j <= n:
        # key concept of the algo
        # this moves the necesary index and rest the unused index
        while cs > s and i < j-1:
            cs = cs - arr[i]
            i = i + 1

        if cs == s:
            return i + 1, j

        if j < n:
            cs = cs + arr[j]
        j = j + 1

    return [-1]


''' 
**************** Move all negative elements to end ****************
Given an unsorted array arr[] of size N having both negative and positive integers.
The task is place all negative element at the end of array without changing the order of positive element and negative element.
'''


def segregate_elements(arr):
    """
    It segregates the negative numbers from the positive numbers in an array.
    
    :param arr: The array to be sorted
    :return: the array with the positive numbers first and the negative numbers second.
    """
    nArr = []
    pArr = []
    for i in arr:
        if i < 0:
            nArr.append(i)
        else:
            pArr.append(i)
    arr = pArr + nArr
    return arr


''' 
**************** Union of two arrays ****************
Given two arrays a[] and b[] of size n and m respectively.
The task is to find union between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
If there are repetitions, then only one occurrence of element should be printed in the union
'''


def union(a, b):
    """
    It takes two lists, and returns the length of the longer list, with the shorter list appended to the
    end of the longer list
    
    :param a: list of integers
    :param b: list of integers
    :return: The length of the longer list.
    """
    if len(a) > len(b):
        for i in b:
            if i not in a:
                b.append(i)
        return len(a)
    else:
        for i in a:
            if i not in b:
                a.append(i)
        return len(b)


def union_ps(a, b):
    """
    It takes two lists, adds them together, converts the result to a set, and returns the length of the
    set
    
    :param a: list of integers
    :param b: the number of times the word appears in the corpus
    :return: The length of the set of the union of the two lists.
    """
    c = a + b
    c = set(c)
    return len(c)
