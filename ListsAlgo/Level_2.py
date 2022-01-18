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


def missing_number_mt(arr, n):
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


def quick_sort(arr):
    '''
    Quick sort, traditional solution and my first
    '''
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
Quick Sort is a Divide and Conquer algorithm.
Given three arrays sorted in increasing order.
Find the elements that are common in all three arrays.
'''


def common_elements_tle(A, B, C):
    '''
    Slow solution
    '''
    commons = set()
    for i in A:
        if (i in A and i in B and i in C):
            commons.add(i)
    commons = list(commons)
    commons = sorted(commons)
    return commons


A = [3, 3, 3]
B = [3, 3, 3]
C = [3, 3, 3]

print(common_elements_tle(A, B, C))
