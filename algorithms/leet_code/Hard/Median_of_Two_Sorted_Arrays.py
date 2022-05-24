# 4. Median of Two Sorted Arrays
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

# 99ms
def findMedianSortedArrays(nums1, nums2):
    """
    Combine the two arrays, sort them, and then return the median of the new array
    
    :param nums1:
    :param nums2:
    :return: The median of the two arrays.
    """
    newArr = nums1 + nums2
    newArr.sort()
    if len(newArr) % 2 ==0:
        return (newArr[int(len(newArr)/2)]+newArr[int(len(newArr)/2)-1])/2
    else:
        return newArr[int(len(newArr)/2)]