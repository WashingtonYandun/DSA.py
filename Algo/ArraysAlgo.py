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
    cont = 0
    pairs = {"Pairs": cont}

    for i in range(0, len(arr)):
        j = i + 1
        for j in range(j, len(arr)):
            if (arr[i] + arr[j] == value):
                cont = cont + 1
                pairs[cont] = [arr[i], arr[j]]

    pairs["Pairs"] = cont
    return pairs


print(sum_of_two_all([0, 2, 49, 5, 4, 9, 6, 24, 10,
      12, -12, 3, 20, 13, 15, 16, 17, 103, 146,
      134, 126, 167, 190, 90, 80, 70, 30, -57, 29,
      36, 29, 21, 25, 22, 68, -67, 69, 1], 1))
