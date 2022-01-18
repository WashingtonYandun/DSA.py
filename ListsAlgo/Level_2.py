# trd == traditional
# ps == python style or using python tricks
# tle == Time Limit Exceeded
# mt == math solution

''' 
**************** Cyclically rotate an array by one ****************
Given an array, rotate the array by one position in clock-wise direction.
'''


def rotate(arr):
    '''
    My first solution
    '''
    arrN = [arr[-1]]
    arr.pop()
    return arrN + arr


def rotate_ps(arr):
    '''
    Using lists
    '''
    arr[:] = arr[-1::] + arr[::-1]
    return arr


''' 
**************** Missing number in array ****************
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.
'''


def MissingNumber_mt(arr, n):
    n = len(arr)+1
    s = n*(n + 1)/2
    cs = sum(arr)
    return int(s - cs)


''' 
**************** Count pairs with given sum ****************
Given an array of N integers, and an integer K,
find the number of pairs of elements in the array whose sum is equal to K.
'''


def getPairsCount_tle(arr, k):
    '''
    My first solution 
    '''
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


def quickSort(self, arr, low, high):
    return 0


def partition(self, arr, low, high):
    return 0
