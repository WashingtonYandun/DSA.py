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
