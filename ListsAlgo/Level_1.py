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
    '''
    return a peak element from an array
    '''
    arr.append(0)
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            return i
    arr.pop()
    return None


def peak_element_ps(arr):
    '''
    return a peak element from an array, using max() (Tricky xd)!
    '''
    return arr.index(max(arr))


def peak_all_element(arr):
    '''
    return a list with all the indexes where exist a peak element in the list given,
    using max() 
    '''
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
    '''
    find and return maximun and minimun elements from an array
    '''
    maximun = 0
    minimun = arr[0]
    # this len(arr) could be replaced for n
    for i in range(len(arr)):
        if arr[i] < minimun:
            minimun = arr[i]
        if arr[i] > maximun:
            maximun = arr[i]
    return minimun, maximun


def get_min_max_ps(arr):
    '''
    find and return maximun and minimun elements from an array,
    using min() and max()
    '''
    return min(arr), max(arr)


''' 
**************** Reverse a String ****************
You are given a string s. You need to reverse the string.
'''


def reverse_word_trd(s):
    '''
    return a reverse string or array
    '''
    sReversed = ""
    for i in range(len(s)-1, -1, -1):
        sReversed = sReversed + s[i]
    return sReversed


def reverse_word_ps(s):
    '''
    return a reverse string or array, using "lists"
    '''
    return s[::-1]


''' 
**************** Sort The Array  ****************
Given a random set of numbers, Print them in sorted order.
'''


def bubble_sort(arr):
    '''
    return a sorted array using bubble sort
    '''
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                # swap variables python style, we could use a temp var
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_list(arr):
    '''
    return a sorted array using sorted()
    '''
    return sorted(arr)


''' 
**************** Kth smallest element ****************
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
'''


def kth_smallest(arr, k):
    '''
    Order the array and return k-1 value of the sorted array
    '''
    # need an optimized solution
    return sorted(arr)[k-1]


''' 
**************** Find the Frequency ****************
Given a vector of N positive integers and an integer X.
The task is to find the frequency of X in vector.
'''


def find_frequency_ps(arr, x):
    '''
    return the number of times x is in the array
    '''
    xFrecuency = 0
    for i in arr:
        if i == x:
            xFrecuency = xFrecuency + 1
    return xFrecuency


def find_frequency_trd(arr, x):
    '''
    return the number of times x is in the array
    '''
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
    '''
    return a sorted array containing 0,1,2 (useless)
    '''
    arr = arr.sort()
    return arr


''' 
**************** Subarray with given sum ****************
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
'''


def sub_array_sum_tle(arr, s):
    '''
    return a subarray with the given sum
    '''
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
    '''
    return a subarray with the given sum
    '''
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
    '''
    put all the negative elements of the array to the end
    '''
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
    '''
    return the lenght of the union of two arrays
    '''
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
    '''
    return the lenght of the union of two arrays using sets set()
    '''
    c = a + b
    c = set(c)
    return len(c)
