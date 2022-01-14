def sum_of_two(arr, value):
    '''
    In a given list if there is a pair of element that matches the sum given, return true.
    '''
    for i in arr:
        diff = value - i
        if diff in arr:
            return True
    return False


def sum_of_two_all(arr, value):
    '''
    Print all the matches of the sum_of_two problem. return true if it exist
    '''
    flag = False
    for i in arr:
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j] == value):
                flag = True
                print([arr[i], arr[j]])
    return flag


sum_of_two_all([1, 2, 3, 4, 5, 6], 10)
