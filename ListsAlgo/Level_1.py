arr = [15, 2, 4, 8, 9, 5, 10, 23]
# trd == traditional
# ps == python style or using python tricks
# tle == Time Limit Exceeded

''' 
**************** PEAK ELEMENT ****************
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.
'''


def peakElement_trd(self, arr, n):
    '''
    Solution given on GG practice
    '''
    arr.append(0)
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            return i
    arr.pop()
    return None


def peakElement_ps(arr):
    '''
    my first solution using max() a litle tricky
    '''
    return arr.index(max(arr))


def peak_all_element(arr):
    '''
    return a list with all the indexes where exist a peak element in the list given
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


def getMinMax_trd(arr, n):
    '''
    Solution given on GG practice
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


def getMinMax_ps(arr):
    '''
    My first solution using min() and max() a litle tricky
    '''
    return min(arr), max(arr)


''' 
**************** Reverse a String ****************
You are given a string s. You need to reverse the string.
'''


def reverseWord_trd(s):
    '''
    My "traditional" solution
    '''
    sReversed = ""
    for i in range(len(s)-1, -1, -1):
        sReversed = sReversed + s[i]
    return sReversed


def reverseWord_ps(s):
    '''
    My first solution, python style
    '''
    return s[::-1]


''' 
**************** Sort The Array  ****************
Given a random set of numbers, Print them in sorted order.
'''


def sortArr(arr):
    '''
    bubble sort, limit time Exceeded
    '''
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                # swap variables python style, we could use a temp var
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sortArr(arr):
    '''
    Solution given to gg, using sorted()
    '''
    return sorted(arr)


''' 
**************** Kth smallest element ****************
Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
'''


def kthSmallest(arr, k):
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


def findFrequency_ps(arr, x):
    '''
    Using python for
    '''
    xFrecuency = 0
    for i in arr:
        if i == x:
            xFrecuency = xFrecuency + 1
    return xFrecuency


def findFrequency_trd(arr, x):
    '''
    Traditional solution
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
    arr = arr.sort()
    return arr


''' 
**************** Sort an array of 0s, 1s and 2s ****************
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
'''


def subArraySum_tle(arr, s):
    '''
    Time Limit Exceeded solution
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


print(subArraySum_tle(arr, 134))
