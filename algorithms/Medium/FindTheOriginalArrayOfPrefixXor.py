# 2433. Find The Original Array of Prefix Xor
'''
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.
'''

class Solution:
    # 555ms, Beats 94.92%
    # 36.64MB, Beats 15.11%
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return [pref[0]]
        
        arr = [pref[0]] 

        for i in range(1, len(pref)):
            arr.append(pref[i-1] ^ pref[i])

        return arr
                

